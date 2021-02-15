import random

player_wins = [856, 671, 831, 144, 329, 677,
               158, 342, 679, 138, 416, 710,
               891, 125, 837, 804, 765, 468,
                ]
print(player_wins)

att_example = [(144, 329, 677), (138, 416, 710), (804, 765, 468)]



att = []
for i in range(len(player_wins) - 3 + 1):
    nums = player_wins[i:i +3]
    if min(nums) >= 300:
        att.append(tuple(nums))
    # print
assert att == att_example, 'wrong result'

