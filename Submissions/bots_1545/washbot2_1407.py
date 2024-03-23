# bot code goes here
from Game.Skills import *
from Game.projectiles import *
from ScriptingHelp.usefulFunctions import *
from Game.playerActions import defense_actions, attack_actions, projectile_actions
from gameSettings import HP, LEFTBORDER, RIGHTBORDER, LEFTSTART, RIGHTSTART, PARRYSTUN

from random import randint


# PRIMARY CAN BE: Teleport, Super Saiyan, Meditate, Dash Attack, Uppercut, One Punch
# SECONDARY CAN BE : Hadoken, Grenade, Boomerang, Bear Trap

# TODO FOR PARTICIPANT: Set primary and secondary skill here
PRIMARY_SKILL = DashAttackSkill
SECONDARY_SKILL = Grenade

#constants, for easier move return
#movements
JUMP = ("move", (0,1))
FORWARD = ("move", (1,0))
BACK = ("move", (-1,0))
JUMP_FORWARD = ("move", (1,1))
JUMP_BACKWARD = ("move", (-1, 1))

# attacks and block
LIGHT = ("light",)
HEAVY = ("heavy",)
BLOCK = ("block",)

PRIMARY = get_skill(PRIMARY_SKILL)
SECONDARY = get_skill(SECONDARY_SKILL)

# no move, aka no input
NOMOVE = "NoMove"
# for testing
moves = SECONDARY,
moves_iter = iter(moves)

# TODO FOR PARTICIPANT: WRITE YOUR WINNING BOT
class Script:
    def __init__(self):
        self.primary = PRIMARY_SKILL
        self.secondary = SECONDARY_SKILL
        
    # DO NOT TOUCH
    def init_player_skills(self):
        return self.primary, self.secondary
    
    # MAIN FUNCTION that returns a single move to the game manager
    def get_move(self, player, enemy, player_projectiles, enemy_projectiles):


        distance = get_distance(player, enemy)
        distance_x = abs(get_pos(player)[0] - get_pos(enemy)[0])

        if 0 <= distance <= 4:
            if distance <= 1:
                if get_primary_skill(enemy) == "onepunch" and not primary_on_cooldown(enemy):
                    if distance_x == 1:
                        return JUMP_BACKWARD
                else:
                    if not secondary_on_cooldown(player):
                        return SECONDARY
                    if not heavy_on_cooldown(player):
                        return HEAVY
                    if get_stun_duration(enemy) != 0:
                        return BLOCK
                    else:
                        return JUMP_BACKWARD

            if not primary_on_cooldown(player):
                return PRIMARY

            if not secondary_on_cooldown(player):
                return SECONDARY

            else:
                return JUMP_BACKWARD

        if 4 < distance < 7:
            if not secondary_on_cooldown(player):
                return SECONDARY

            if not primary_on_cooldown(player):
                return PRIMARY

            
            else:
                if randint(0,1):
                    return BLOCK
                else:
                    return FORWARD

        if distance >= 7:
            return JUMP_FORWARD
        

