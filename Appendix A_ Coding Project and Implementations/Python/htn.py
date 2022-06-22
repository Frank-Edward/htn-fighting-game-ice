class state():
    def __init__(self, name):
        self.name = name
        self.preconditions = {}
        self.tasks = []
        self.action = None

## STATE CREATION

Act = state("Act")


avoid_projectile = state("avoid_projectile")
escape_corner = state("escape_corner")
landing_action = state("landing_action")
anti_air = state("anti_air")
use_combo = state("use_combo")
use_attack_skill = state("use_attack_skill")
move = state("move")


jump_in_place = state("jump_in_place")
jump_foreward = state("jump_foreward")
guard = state("guard")

jump_out = state("jump_out")
dash_foreward = state("dash_foreward")
#super_out

high_arial = state("high_arial")
low_arial = state("low_arial")

use_super = state("use_super")
use_normal = state("use_normal")
dash_under = state("dash_under")

start_combo = state("start_combo")
continue_combo = state("continue_combo")

''' NEW ACTION NEW ACTION NEW ACTION '''
high_energy_proj = state("high_energy_proj")
guard_low = state("guard_low")
'''NEW ACTION'''
sliding_attack = state("sliding_attack")
knock_back_attack = state("knock_back_attack")
knock_down_attack = state("knock_down_attack")
projectile_attack = state("projectile_attack")

come_closer = state("come_closer")
keep_distance = state("keep_distance")


second_hit = state("second_hit")
third_hit = state("third_hit")
fouth_hit = state("fourth_hit")

high_energy = state("high_energy") 
low_energy = state("low_energy")

jump_in = state("jump_in")
dash_in = state("dash_in")
walk = state("walk")

#projectile_attack
step_back = state("step_back")


## PRECONDITIONS

Act.preconditions = {"char_actionable":True}


avoid_projectile.preconditions = {"char_gnd":True, "opp_proj":True} 
escape_corner.preconditions = {"char_gnd":True,"char_in_corner":True}
landing_action.preconditions = {"char_gnd": False}
anti_air.preconditions = {"char_gnd": True, "opp_gnd":False}
use_combo.preconditions = {"char_gnd":True}
use_attack_skill.preconditions = {"char_gnd":True}
move.preconditions = {"char_gnd":True}


jump_in_place.preconditions = {"char_med_x":True}
jump_foreward.preconditions = {"char_long_x":True}
guard.preconditions = {"char_short_x":True}

jump_out.preconditions = {"opp_gnd":True}
dash_foreward.preconditions = {"opp_gnd":False, "opp_short_y":False}
#super_out

high_arial.preconditions = {"opp_gnd":False, "char_short_y":True, "char_short_x":True}
low_arial.preconditions = {"opp_gnd":True, "char_short_x":True}

use_super.preconditions = {"char_short_x":True, "char_energy_high":True, "char_short_y":False}
use_normal.preconditions = {"char_short_x":True, "char_short_y":False}
dash_under.preconditions = {"char_short_x":False} #maybe too risky

start_combo.preconditions = {"char_combo":False, "opp_gnd":True, "char_short_x":True}
continue_combo.preconditions = {"char_combo":True}

'''NEW'''
high_energy_proj.preconditions = {"char_energy_high":True, "char_long_x":False, "char_combo":True}
guard_low.preconditions = {"char_combo":True, "opp_energy_low":True}

'''NEW'''
sliding_attack.preconditions = {"char_energy_low":True, "char_long_x":False, "char_short_y":True}
knock_back_attack.preconditions = {"char_med_x":True, "opp_energy_high":False}
knock_down_attack.preconditions = {"char_med_x":True, "opp_energy_high":True, "opp_gnd":True}
projectile_attack.preconditions = {"char_long_x":True}

come_closer.preconditions = {"char_short_x":False}
keep_distance.preconditions = {"opp_energy_high":True}#camp? unsure how this will work


second_hit.preconditions = {"char_1":True}
third_hit.preconditions = {"char_2":True, "opp_energy_low":False}
fouth_hit.preconditions = {"char_3":True}

high_energy.preconditions = {"char_energy_high":True}
low_energy.preconditions = {"char_min_energy":True, "opp_energy_high":False}

jump_in.preconditions = {"char_long_x":True, "opp_gnd":True}
dash_in.preconditions = {"char_long_x":True}
walk.preconditions = {"char_med_x":True}

#projectile_attack
step_back.preconditions = {"char_energy_high":True}




## SUBTASKS / PRIMATIVES

Act.tasks = [avoid_projectile, escape_corner, landing_action, anti_air, use_combo, use_attack_skill, move]


avoid_projectile.tasks = [jump_in_place, jump_foreward, guard]
escape_corner.tasks = [jump_out,  dash_foreward]
landing_action.tasks = [high_arial, low_arial]
anti_air.tasks = [use_super, use_normal, dash_under]
use_combo.tasks = [start_combo, continue_combo]
use_attack_skill.tasks = [high_energy_proj, sliding_attack, guard_low, knock_back_attack, knock_down_attack, projectile_attack]
move.tasks = [come_closer, keep_distance]


jump_in_place.tasks = []
jump_foreward.tasks = []
guard.tasks = []

jump_out.tasks = []
dash_foreward.tasks = []
#super_out

high_arial.tasks = []
low_arial.tasks = []

use_super.tasks = []
use_normal.tasks = []
dash_under.tasks = []

start_combo.tasks = []
continue_combo.tasks = [second_hit, third_hit, fouth_hit]

high_energy_proj.tasks = []
guard_low.tasks = []

sliding_attack.tasks = []
knock_back_attack.tasks = []
knock_down_attack.tasks = []
projectile_attack.tasks = [high_energy, low_energy]

come_closer.tasks = [jump_in, dash_in, walk]
keep_distance.tasks = [projectile_attack, step_back]


second_hit.tasks = []
third_hit.tasks = []
fouth_hit.tasks = [use_attack_skill]

high_energy.tasks = []
low_energy.tasks = []

jump_in.tasks = []
dash_in.tasks = []
walk.tasks = []

#projectile_attack
step_back.tasks = []


## ACTIONS

Act.action = None


avoid_projectile.action = None
escape_corner.action = None
landing_action.action = None
anti_air.action = None
use_combo.action = None
use_attack_skill.action = None
move.action = None


jump_in_place.action = "JUMP"
jump_foreward.action = "FOR_JUMP"
guard.action = "FOR_JUMP"#"STAND_GUARD"

jump_out.action = "FOR_JUMP"
dash_foreward.action = "CROUCH_B" #Crouch_guard
#super_out

high_arial.action = "AIR_DB"
low_arial.action = "AIR_B"
 
use_super.action = "STAND_F_D_DFB"
use_normal.action =  "CROUCH_FA" #"CROUCH_FA"
dash_under.action = "DASH" #"STAND_F_D_DFA" #"DASH"

start_combo.action = "STAND_A"
continue_combo.action = None

high_energy_proj.action = "STAND_D_DF_FC"
guard_low.action = "AIR_DB" #see if jumps #"CROUCH_GUARD"
sliding_attack.action = "STAND_D_DB_BB"
knock_back_attack.action = "STAND_B" #change back to b 
knock_down_attack.action = "CROUCH_FB"
projectile_attack.action = None

come_closer.action = None
keep_distance.action = None


second_hit.action = "STAND_B" #"STAND_B"
third_hit.action = "STAND_FA" #"STAND_FA"
fouth_hit.action = None#"STAND_D_DB_BB"#need yo add options here

high_energy.action = "STAND_D_DF_FC"
low_energy.action = "STAND_D_DF_FB"

jump_in.action = "FOR_JUMP"
dash_in.action = "DASH"
walk.action = "FORWARD_WALK" #"FOREWARD_WALK" #FOR SOME RASON THIS DOENT WORL

#projectile_attack
step_back.action = "BACK_STEP"



def decompose(compound, Conditions):
    broken = False
    #print("IN DECOMPOSE")

    if not compound.tasks:
        for precondition in compound.preconditions:
            if Conditions[precondition] != compound.preconditions[precondition]:
                #print("nothing here")
                return None
        #print("returning compound action", compound.action)
        return compound.action
    else:
        action = None
        for task in compound.tasks:
            for precondition in task.preconditions:
                if Conditions[precondition] != task.preconditions[precondition]:
                    broken = True
                    break
            if broken:
                broken = False
            else:
                action = decompose(task, Conditions)
                broken = False
            if action != None:
                #print("returning action", action)

                return action
    return action
            
def plan(start_task, Conditions):
    # print("Plan start *********************************")
    # print(start_task.__name__)
    # print(Conditions)
    action = None
    broken = False
    for task in start_task.tasks:
        for precondition in task.preconditions:
            #print("Conditions: ", Conditions[precondition])
            #print("Conditions)
            if Conditions[precondition] != task.preconditions[precondition]:
                broken = True
                break
        if broken:
            #print("broken")
            broken = False
        else:
            #print("IN HERE")
            action = decompose(task, Conditions)
            #print("action from decompose : ", action)
            broken = False
        if action != None:
            return action
    #print(action)
    #print("Plan END *********************************")
    return "STAND_B"


'''
Conditions = {
    "char_air":True,
    "char_gnd":True,
    "char_short_x":True,
    "char_short_y":True,
    "char_med_x":True,
    "char_med_y":True,
    "char_long_x":True, 
    "char_long_y":True,
    "char_energy_high":True,
    "char_energy_low":True,
    "char_combo":True,
    "char_in_corner":True,
    "char_proj":True,
    
    "opp_air":True,
    "opp_gnd":True,
    "opp_short_x":True,
    "opp_short_y":True,
    "opp_med_x":True,
    "opp_med_y":True,
    "opp_long_x":True, 
    "opp_long_y":True,
    "opp_energy_high":True,
    "opp_energy_low":True,
    "opp_combo":True,
    "opp_in_corner":True,
    "opp_proj":True,
}
'''
