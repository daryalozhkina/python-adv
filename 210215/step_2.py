player_wins = [856, 671, 831, 144, 329, 677,
               158, 342, 679, 138, 416, 710,
               891, 125, 837, 804, 765, 468,
                ]
print(player_wins)

att_example = [(144, 329, 677), (138, 416, 710), (804, 765, 468)]

att = []


for nums in zip(player_wins, player_wins[1:], player_wins[2:]):
    if min(nums) >= 300:
        att.append(tuple(nums))
    print(nums)
