def get_checked_tiles(pos, attack_data):

    attack_list = []
    attack_options = []




    for i, m in enumerate(attack_data):
        if (i % 2) == 0:
            i = pos[0] + m

            attack_list.append(i)
        else:
            n = pos[1] + m

            attack_list.append(n)
        if len(attack_list) >= 2:
            for check in attack_list:
                if check > 660 or check < 80:
                    attack_list = []

            attack_options.append(attack_list)
            attack_list = []

        #  Enemy list is added to attack data to determine where the piece will actually consider an attack
    attack_options = [v for v in attack_options if v != []]


    return attack_options