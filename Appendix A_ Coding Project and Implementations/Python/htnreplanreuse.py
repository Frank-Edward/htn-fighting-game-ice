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

high_energy_proj = state("high_energy_proj")
guard_low = state("guard_low")
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

high_energy_proj.preconditions = {"char_energy_high":True, "char_long_x":False, "char_combo":True}
guard_low.preconditions = {"char_combo":True, "opp_energy_low":True}

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


## Outconditions

Act.outconditions = {}


avoid_projectile.outconditions = {} 
escape_corner.outconditions = {}
landing_action.outconditions = {}
anti_air.outconditions = {}
use_combo.outconditions = {}
use_attack_skill.outconditions = {}
move.outconditions = {}


jump_in_place.outconditions = {"char_gnd":False}
jump_foreward.outconditions = {"char_gnd":False, "char_med_x":True, "char_long_x":False}
guard.outconditions = {}

jump_out.outconditions = {"char_gnd":False}
dash_foreward.outconditions = {}
#super_out

high_arial.outconditions = {"char_gnd":True, "opp_gnd":True, "char_combo":True}
low_arial.outconditions = {"opp_gnd":True, "char_gnd":True, "char_combo":True}

use_super.outconditions = {"char_short_x":False, "char_med_x":True, "char_energy_high":False, "char_short_y":True, "char_med_y":False, "char_long_y":False, "opp_gnd":True}
use_normal.outconditions = {"char_short_x":True, "char_long_y":False, "char_short_y":True, "char_med_y":False, "opp_gnd":True}
dash_under.outconditions = {"char_short_y":True, "char_long_y":False, "char_med_y":False, "opp_gnd":True}

start_combo.outconditions = {"char_combo":True, "char_1":True}
continue_combo.outconditions = {}

high_energy_proj.outconditions = {"char_energy_high":False,"char_energy_low":False, "char_combo":False, "char_med_x":False, "char_short_x":False, "char_long_x":True}
guard_low.outconditions = {"char_combo":False, "char_short_x":True}

sliding_attack.outconditions = {"char_energy_low":True, "char_long_x":False, "char_long_y":False, "char_short_x":True, "char_med_x":False}
knock_back_attack.outconditions = {"char_combo":True}
knock_down_attack.outconditions = {"char_combo":True}
projectile_attack.outconditions = {"char_proj":True}

come_closer.outconditions = {"char_short_x":True}
keep_distance.outconditions = {"opp_energy_high":True}#camp? unsure how this will work


second_hit.outconditions = {"char_1":False, "char_2":True}
third_hit.outconditions = {"char_2":False, "char_3":True}
fouth_hit.outconditions = {"char_3":False, "char_combo":False}

high_energy.outconditions = {"char_energy_high":False, "char_energy_low":False}
low_energy.outconditions = {"char_min_energy":False}

jump_in.outconditions = {"char_long_x":False, "char_med_x":True}
dash_in.outconditions = {"char_long_x":False, "char_med_x":True}
walk.outconditions = {"char_med_x":False, "char_short_x":True}

#projectile_attack
step_back.outconditions = {"char_energy_low":False}



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
guard.action = "FOR_JUMP"

jump_out.action = "FOR_JUMP"
dash_foreward.action = "CROUCH_B" 

high_arial.action = "AIR_DB"
low_arial.action = "AIR_B"
 
use_super.action = "STAND_F_D_DFB"
use_normal.action =  "CROUCH_FA" 
dash_under.action = "DASH" 

start_combo.action = "STAND_A"
continue_combo.action = None

high_energy_proj.action = "STAND_D_DF_FC"
guard_low.action = "AIR_DB" 
sliding_attack.action = "STAND_D_DB_BB"
knock_back_attack.action = "STAND_B"
knock_down_attack.action = "CROUCH_FB"
projectile_attack.action = None

come_closer.action = None
keep_distance.action = None


second_hit.action = "STAND_B"
third_hit.action = "STAND_FA" 
fouth_hit.action = None

high_energy.action = "STAND_D_DF_FC"
low_energy.action = "STAND_D_DF_FB"

jump_in.action = "FOR_JUMP"
dash_in.action = "DASH"
walk.action = "FORWARD_WALK"

#projectile_attack
step_back.action = "BACK_STEP"


## full preconditions for ease of computing:
return_preconditions = {}
return_preconditions["jump_in_place"] = {"char_gnd":True, "opp_proj":True, "char_med_x":True, "char_short_x":False, "char_long_x":False}
return_preconditions["jump_foreward"] = {"char_gnd":True, "opp_proj":True, "char_long_x":True, "char_med_x":False, "char_short_x":False}
return_preconditions["guard"] = {"char_gnd":True, "opp_proj":True, "char_short_x":True, "char_med_x":False, "char_long_x":False}
return_preconditions["jump_out"] = {"char_gnd":True,"char_in_corner":True, "opp_gnd":True, "opp_proj":False}
return_preconditions["dash_foreward"] =  {"char_gnd":True,"char_in_corner":True, "opp_gnd":False, "opp_short_y":False, "opp_proj":False}
return_preconditions["high_arial"] = {"char_gnd": False, "opp_gnd":False, "char_short_y":True, "char_short_x":True, "opp_proj":False}
return_preconditions["low_arial"] ={"char_gnd": False, "opp_gnd":True, "char_short_x":True, "opp_proj":False}
return_preconditions["use_super"] = {"char_gnd": True, "opp_gnd":False, "char_short_x":True, "char_energy_high":True, "char_short_y":False, "opp_proj":False}
return_preconditions["use_normal"] = {"char_gnd": True, "opp_gnd":False, "char_short_x":True, "char_long_y":False, "char_short_y":False, "opp_proj":False}
return_preconditions["dash_under"] = {"char_gnd": True, "opp_gnd":False, "char_short_y":False, "opp_proj":False}
return_preconditions["start_combo"] = {"char_gnd":True, "char_short_x":True, "char_combo":False, "opp_proj":False}
return_preconditions["high_energy_proj"] = {"char_gnd":True, "char_short_x":False,"char_energy_high":True, "char_combo":True, "opp_proj":False}
return_preconditions["guard_low"] = {"char_gnd":True, "char_short_x":True,"opp_energy_low":True, "char_combo":False, "opp_proj":False}
return_preconditions["sliding_attack"] =  {"char_gnd":True, "char_energy_low":True, "char_long_x":False, "char_long_y":False, "opp_proj":False}
return_preconditions["knock_back_attack"] = {"char_gnd":True, "char_short_x":True, "opp_energy_high":False, "opp_proj":False}
return_preconditions["knock_down_attack"] = {"char_gnd":True, "char_short_x":True, "opp_energy_high":True, "opp_proj":False}
return_preconditions["second_hit"] = {"char_gnd":True, "char_short_x":True, "char_combo":True,"char_1":True, "opp_proj":False}
return_preconditions["third_hit"] = {"char_gnd":True, "char_short_x":True, "char_combo":True,"char_2":True, "opp_proj":False}
return_preconditions["high_energy"] = {"char_gnd":True, "char_short_x":False, "char_energy_high":True}
return_preconditions["low_energy"] = {"char_gnd":True, "char_short_x":False, "char_min_energy":True, "opp_energy_high":False, "opp_proj":False}
return_preconditions["jump_in"] =  {"char_gnd":True, "char_short_x":False, "char_long_x":True, "opp_gnd":True, "opp_proj":False}
return_preconditions["dash_in"] = {"char_gnd":True, "char_short_x":False, "char_long_x":True, "opp_proj":False}
return_preconditions["walk"] = {"char_gnd":True, "char_short_x":False, "char_med_x":True, "opp_proj":False}
return_preconditions["step_back"] = {"char_gnd":True, "opp_energy_high":True, "char_energy_low":False, "opp_proj":False}


##Prioritized decomposition

prioritized_decomposition = {
    "avoid_projectile": [avoid_projectile, escape_corner, landing_action, anti_air, use_combo, use_attack_skill, move],
    "escape_corner": [escape_corner, avoid_projectile, landing_action, anti_air, use_combo, use_attack_skill, move],
    "landing_action": [landing_action, escape_corner, anti_air, avoid_projectile, use_combo, use_attack_skill, move],
    "anti_air": [anti_air, landing_action, use_combo,  escape_corner, use_attack_skill, avoid_projectile, move],
    "use_combo":[use_combo, anti_air, use_attack_skill, landing_action, move,  escape_corner, avoid_projectile],
    "use_attack_skill": [use_attack_skill, use_combo, move, anti_air, landing_action,  escape_corner, avoid_projectile],
    "move": [move, use_attack_skill, use_combo,anti_air, landing_action, escape_corner, avoid_projectile]
}


##function

def decompose(compound, Conditions, return_preconditions):
    broken = False
    #print("IN DECOMPOSE")

    if not compound.tasks:
        for precondition in compound.preconditions:
            if Conditions[precondition] != compound.preconditions[precondition]:
                #print("nothing here")
                return None, None, None
        #print("returning compound action", compound.action)
        return compound.action, return_preconditions[compound.name], compound.outconditions
    else:
        action = None
        outconditions = None
        ret_pre = None
        for task in compound.tasks:
            for precondition in task.preconditions:
                if Conditions[precondition] != task.preconditions[precondition]:
                    broken = True
                    break
            if broken:
                broken = False
            else:
                action, ret_pre, outconditions = decompose(task, Conditions, return_preconditions)
                broken = False
            if action != None:
                #print("returning action", action)

                return action,ret_pre, outconditions
    return action, ret_pre, outconditions
            
def plan(start_task, Conditions, return_preconditions):
    # print("Plan start *********************************")
    # print(start_task.__name__)
    # print(Conditions)
    action = None
    outconditions = None
    ret_pre = None
    broken = False
    tasks = prioritized_decomposition[start_task]
    for task in tasks:
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
            action, ret_pre, outconditions = decompose(task, Conditions, return_preconditions)
            #print("action from decompose : ", action)
            broken = False
        if action != None:
            return action, ret_pre, outconditions, task.name
    #print(action)
    #print("Plan END *********************************")
    return "STAND_B", {"char_actionable":False}, {}, avoid_projectile.name


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


