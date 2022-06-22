from py4j.java_gateway import get_field
from htnreplan import *


class HtnAI(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.plan_state = "ready" 
        self.count = 0
        self.first = False
        self.prev = "STAND"
        self.current = "STAND"
        self.Conditions = {}
        self.priorConditions = {}
        self.plan = []
        self.action = "STAND"
        self.actionConditions = {}
        self.planConditions = []
        
        self.actionCommands = {
            "JUMP": self.gateway.jvm.enumerate.Action.JUMP,
            "FOR_JUMP": self.gateway.jvm.enumerate.Action.FOR_JUMP,
            "CROUCH_B" : self.gateway.jvm.enumerate.Action.CROUCH_B,
            "AIR_DB": self.gateway.jvm.enumerate.Action.AIR_DB,
            "AIR_B": self.gateway.jvm.enumerate.Action.AIR_B,
            "STAND_F_D_DFB": self.gateway.jvm.enumerate.Action.STAND_F_D_DFB,
            "CROUCH_FA": self.gateway.jvm.enumerate.Action.CROUCH_FA,
            "DASH": self.gateway.jvm.enumerate.Action.DASH,
            "STAND_A": self.gateway.jvm.enumerate.Action.STAND_A,
            "STAND_D_DF_FC": self.gateway.jvm.enumerate.Action.STAND_D_DF_FC,
            "STAND_D_DB_BB": self.gateway.jvm.enumerate.Action.STAND_D_DB_BB,
            "STAND_B": self.gateway.jvm.enumerate.Action.STAND_B,
            "CROUCH_FB": self.gateway.jvm.enumerate.Action.CROUCH_FB,
            "STAND_FA": self.gateway.jvm.enumerate.Action.STAND_FA,
            "STAND_D_DF_FB": self.gateway.jvm.enumerate.Action.STAND_D_DF_FB,
            "FORWARD_WALK": self.gateway.jvm.enumerate.Action.FORWARD_WALK,
            "BACK_STEP": self.gateway.jvm.enumerate.Action.BACK_STEP
        
        }
        
    def close(self):
        pass

    def getInformation(self, frameData, isControl):
        # Load the frame data every time getInformation gets called
        self.frameData = frameData
        self.cc.setFrameData(self.frameData, self.player)
        
        # please define this method when you use FightingICE version 3.20 or later
    def roundEnd(self, x, y, z):
        print(1 if x>y else 0, end = "")

        # please define this method when you use FightingICE version 4.00 or later
    def getScreenData(self, sd):
        pass


    def initialize(self, gameData, player):
        # Initializng the command center, the simulator and some other things
        self.inputKey = self.gateway.jvm.struct.Key()
        self.frameData = self.gateway.jvm.struct.FrameData()
        self.cc = self.gateway.jvm.aiinterface.CommandCenter()
        self.player = player
        self.gameData = gameData
        self.simulator = self.gameData.getSimulator()
        self.isGameJustStarted = True

        return 0

    def input(self):
        # The input is set up to the global variable inputKey
        # which is modified in the processing part
        return self.inputKey
        
    def getConditions(self, player):
        
        Conditions = {} 
                   
        self.cc.setFrameData(self.frameData, player)
        distance_x = self.frameData.getDistanceX()
        distance_y = self.frameData.getDistanceY()
        
        char = self.frameData.getCharacter(player)
        char_energy = char.getEnergy()
        char_x = char.getX()
        char_y = char.getY()
        char_state = char.getState()
        
        opp = self.frameData.getCharacter(not player)
        opp_energy = char.getEnergy()
        opp_x = opp.getX()
        opp_y = opp.getY()
        opp_state = opp.getState()
        
        x_diff = char_x - opp_x
        y_diff = char_y - opp_y
        
        #print("differences", x_diff, y_diff)
        
        char_proj =  self.frameData.getProjectilesByP1() if player else self.frameData.getProjectilesByP2()
        opp_proj =  self.frameData.getProjectilesByP1() if not player else self.frameData.getProjectilesByP2()
        
        Conditions["char_actionable"] = True
        Conditions["opp_actionable"] = True
            
        #AIR or GN
        if char_state.equals(self.gateway.jvm.enumerate.State.AIR) or char_state.equals(self.gateway.jvm.enumerate.State.DOWN):
            Conditions["char_gnd"] = False
        else:
            Conditions["char_gnd"] = True
        if opp_state.equals(self.gateway.jvm.enumerate.State.AIR) or opp_state.equals(self.gateway.jvm.enumerate.State.DOWN):
            Conditions["opp_gnd"] = False
        else:
            Conditions["opp_gnd"] = True
        
        #close, med, or far x 
        if distance_x > 310: #310 reiwa
            Conditions["char_short_x"] = False
            Conditions["char_med_x"] = False
            Conditions["char_long_x"] = True
            Conditions["opp_short_x"] = False
            Conditions["opp_med_x"] = False
            Conditions["opp_long_x"] = True
        elif distance_x > 110:#156-160, 110 work for mrASH #110 reiwa
            Conditions["char_short_x"] = False
            Conditions["char_med_x"] = True
            Conditions["char_long_x"] = False
            Conditions["opp_short_x"] = False
            Conditions["opp_med_x"] = True
            Conditions["opp_long_x"] = False
        else:
            Conditions["char_short_x"] = True
            Conditions["char_med_x"] = False
            Conditions["char_long_x"] = False
            Conditions["opp_short_x"] = True
            Conditions["opp_med_x"] = False
            Conditions["opp_long_x"] = False
        #close, med, or far y 
        if distance_y > 160:
            Conditions["char_short_y"] = False
            Conditions["char_med_y"] = False
            Conditions["char_long_y"] = True
            Conditions["opp_short_y"] = False
            Conditions["opp_med_y"] = False
            Conditions["opp_long_y"] = True
        elif distance_y > 25:
            Conditions["char_short_y"] = False
            Conditions["char_med_y"] = True
            Conditions["char_long_y"] = False
            Conditions["opp_short_y"] = False
            Conditions["opp_med_y"] = True
            Conditions["opp_long_y"] = False
        else:
            Conditions["char_short_y"] = True
            Conditions["char_med_y"] = False
            Conditions["char_long_y"] = False
            Conditions["opp_short_y"] = True
            Conditions["opp_med_y"] = False
            Conditions["opp_long_y"] = False
        
        #Set energy
        if char_energy >= 150:
            Conditions["char_energy_high"] = True
            Conditions["char_energy_low"] = True
        elif char_energy>= 50:
            Conditions["char_energy_high"] = False
            Conditions["char_energy_low"] = True
        else:
            Conditions["char_energy_high"] = False
            Conditions["char_energy_low"] = False
        if opp_energy >= 130:
            Conditions["opp_energy_high"] = True
            Conditions["opp_energy_low"] = True
        elif opp_energy>= 30:
            Conditions["opp_energy_high"] = False
            Conditions["opp_energy_low"] = True
        else:
            Conditions["opp_energy_high"] = False
            Conditions["opp_energy_low"] = False
        
        #set_min_energy
        if char_energy >= 30:
            Conditions["char_min_energy"] = True
        else:
            Conditions["char_min_energy"] = False
        
        #Projectiles
        if char_proj:
            Conditions["char_proj"] = True
        else:
            Conditions["char_proj"] = False
        if opp_proj:
            Conditions["opp_proj"] = True
        else:
            Conditions["opp_proj"] = False
        
        #in_corner
        #print(char_x, x_diff)
        
        if (distance_x <= 350) and (((char_x <= 50) and (x_diff < -100)) or ((char_x >= 550) and x_diff > 100)):#maybe revisit to fix again
            Conditions["char_in_corner"] = True
        else:
            Conditions["char_in_corner"] = False
        
        #check combo
        hit = char.getHitCount()
        
        if hit ==0:
            Conditions["char_combo"] = False
            Conditions["char_1"] = False
            Conditions["char_2"] = False
            Conditions["char_3"] = False
        elif hit == 1:
            Conditions["char_combo"] = True
            Conditions["char_1"] = True
            Conditions["char_2"] = False
            Conditions["char_3"] = False
        elif hit == 2:
            Conditions["char_combo"] = True
            Conditions["char_1"] = False
            Conditions["char_2"] = True
            Conditions["char_3"] = False
        elif hit == 3:
            Conditions["char_combo"] = True
            Conditions["char_1"] = False
            Conditions["char_2"] = False
            Conditions["char_3"] = True
        else:
            Conditions["char_combo"] = False
            Conditions["char_1"] = False
            Conditions["char_2"] = False
            Conditions["char_3"] = False
        
        
        #Sprint("x,y:", distance_x, distance_y)

        
        
        return Conditions
        
        
        
        

    def processing(self):
        
        if self.frameData.getEmptyFlag() or self.frameData.getRemainingFramesNumber() <= 0:
                self.isGameJustStarted = True
                return
        if not self.isGameJustStarted:
            # Simulate the delay and look ahead 2 frames. The simulator class exists already in FightingICE
            opp = not self.player
            opp_Conditions = self.getConditions(opp)
            opp_plan, _, __ = plan(Act, opp_Conditions, return_preconditions)
            actions = self.gateway.jvm.java.util.ArrayDeque()
            actions.add(self.actionCommands[opp_plan])
            self.frameData = self.simulator.simulate(self.frameData, self.player, None, actions, 17) #simulating opponenet action
        else:
            # If the game just started, no point on simulating
            self.isGameJustStarted = False
        
        if not self.plan:
            self.priorConditions = self.getConditions(self.player) #should i have something else here

        #print(self.plan)
        
        #print(self.Conditions)
        if len(self.plan) < 4:
            val, preconditions, conditions = plan(Act, self.priorConditions, return_preconditions)
            for condition in conditions:
                self.priorConditions[condition] = conditions[condition] 
            self.plan += [val]
            self.planConditions += [preconditions]

        if self.cc.getSkillFlag(): #does not cover ariels, and something for inactionable
            self.inputKey = self.cc.getSkillKey()
            self.action = self.plan.pop(0)
            self.actionConditions = self.planConditions.pop(0)
            self.Conditions = self.getConditions(self.player)
            for condition in self.actionConditions:
                if self.Conditions[condition] != self.actionConditions[condition]:
                    #print("\n plan failed")
                    self.frameData = self.simulator.simulate(self.frameData, self.player, None, None, 17) #get data again, with no actions
                    val, preconditions, conditions = plan(Act, self.Conditions, return_preconditions)
                    self.plan = []
                    self.planConditions = []
                    self.actionConditions = {}#should have something with output conditions in here
                    return
            #print("\n plan sucess")
            return
        
        self.inputKey.empty()
        self.cc.skillCancel()
        #print(self.action, end = " ")
        self.cc.commandCall(self.action)
        
    class Java:
        implements = ["aiinterface.AIInterface"]
