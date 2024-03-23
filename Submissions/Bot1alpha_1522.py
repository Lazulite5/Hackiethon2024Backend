# bot code goes here
import random
from Game.Skills import *
from Game.projectiles import *
from ScriptingHelp.usefulFunctions import *
from Game.playerActions import defense_actions, attack_actions, projectile_actions
from Game.gameSettings import HP, LEFTBORDER, RIGHTBORDER, LEFTSTART, RIGHTSTART, PARRYSTUN


# PRIMARY CAN BE: Teleport, Super Saiyan, Meditate, Dash Attack, Uppercut, One Punch
# SECONDARY CAN BE : Hadoken, Grenade, Boomerang, Bear Trap

# TODO FOR PARTICIPANT: Set primary and secondary skill here
PRIMARY_SKILL = Meditate
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
CANCEL = ("skill_cancel", )

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
        
        # long distance control flow
        if distance > 5:
            # Meditate again if cooldown allows and if hp is low
            if not primary_on_cooldown(player) or get_hp(player) < 20:
                return PRIMARY
            return FORWARD  # move towards enemy if too far from them
        
        # if very close to enemy, spam either heavy, light attacks or a block enemy has had cooldown already    
        if distance == 1:
            if not heavy_on_cooldown(player):
                return HEAVY
            elif heavy_on_cooldown(enemy) == 0 or primary_on_cooldown(enemy) == 0 or secondary_on_cooldown(enemy) == 0:
                return BLOCK
            elif get_stun_duration(enemy) > 0:
                return LIGHT
            # one punch prevention
            elif get_primary_skill(enemy) == OnePunchSkill and get_primary_cooldown(enemy) == 0:
                return JUMP
            else:
                return LIGHT
        # Meditate if distance is less than 5 (and it not already on cooldown) -- equal to its range
        elif distance <= 3:
            if not primary_on_cooldown(player):
                return PRIMARY
                      
            # otherwise execute secondary skill (Grenade) if primary on cooldown        
            elif not secondary_on_cooldown(player):
                return SECONDARY
        
            # if both on cooldown, jump back to avoid attacks
            elif abs(get_pos(player)[0] - get_proj_pos(enemy)[0]) == 1:
                return JUMP_BACKWARD
            #return NOMOVE
            
             

        
