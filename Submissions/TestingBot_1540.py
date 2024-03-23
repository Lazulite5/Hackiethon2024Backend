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
PRIMARY_SKILL = Meditate
SECONDARY_SKILL = Hadoken

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
        self.current_tick = 0
    # DO NOT TOUCH
    def init_player_skills(self):
        return self.primary, self.secondary
    
    # MAIN FUNCTION that returns a single move to the game manager
    def get_move(self, player, enemy, player_projectiles, enemy_projectiles):
        self.current_tick += 1
        if self.current_tick == 120 and get_primary_cooldown(player) == 0:
            return PRIMARY

        distance = abs(get_pos(player)[0] - get_pos(enemy)[0])

        # if get_primary_skill(enemy) != DashAttackSkill:
        if get_primary_cooldown(player) == 0:
            if get_hp(player) < 90:
                return PRIMARY
        
        if get_secondary_cooldown(player) == 0:
            if get_secondary_skill(enemy) == Hadoken:
                distance2 = abs(get_pos(player)[0] - get_pos(enemy_projectiles)[0])
                if distance2 == 1:
                    return BLOCK
            return SECONDARY

        if distance == 1:
            if get_stun_duration(enemy) != 0:
                return LIGHT
            if get_primary_skill(enemy) == OnePunchSkill and get_primary_cooldown(enemy) == 1:
                return JUMP
            return BLOCK
        if get_secondary_skill(enemy) == Grenade or get_primary_skill(enemy) == UppercutSkill:
            # calculate the distance with projectile 
            distance2 = abs(get_pos(player)[0] - get_pos(enemy_projectiles)[0])
            if 0 <= distance2 <= 2:
                if get_pos(player)[0] <= 3:
                    return JUMP_FORWARD
                else:
                    return JUMP_BACKWARD
        return JUMP_FORWARD
        # else:
        #     if get_primary_cooldown(player) == 0:
        #         if get_hp(player) < 80:
        #             return PRIMARY
        #     if get_secondary_cooldown(player) == 0:
        #         return SECONDARY
        #     if distance == 1:
        #         if get_stun_duration(enemy) != 0:
        #             return LIGHT
        #         else:
        #             return BLOCK
        #     else:
        #         return JUMP_FORWARD