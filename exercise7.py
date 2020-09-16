
def moves_to_show_same_number_of_pips(dice):
    # If we want all dice have the same number of pips, say 5
    # Then we could know that there are in total three types of dice:
    # 1. Dice that have 5 as tips (We need to flip 0 times) - X
    # 2. Dice that have 2(opposite of 5) as tips (We need to flip twice) - Y
    # 3. Dice that have different tips other than 5 or 2 (We need to flip once) - Z
    #
    # If we have Y of type 1 dice, X of type 2 dice and Z - X - Y type 3 dice
    # Then the number of flips equals to Z + X - Y
    # So we only need to calculate the minimum of X - Y

    # Get the number of dice that have different tips
    dice_dict = dict()
    for die in dice:
        if die not in dice_dict:
            dice_dict[die] = 1
        else:
            dice_dict[die] += 1

    # Get the minimum of X - Y
    minimum = []
    for die in dice_dict:
        if (7 - die) in dice_dict:
            minimum.append(dice_dict[7 - die] - dice_dict[die])
        else:
            minimum.append(0 - dice_dict[die])

    return len(dice) + min(minimum)
