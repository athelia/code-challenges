import pdb


def largest_seq(lst):
    my_dict = {}
    keys_list = []
    for i in range(len(lst)):
        if i == 0:
            my_dict[(0, 0)] = lst[0]
            keys_to_add = [(0, 0)]
        else:
            keys_to_add = []
            for key in keys_list:
                # pdb.set_trace()
                my_dict[(key[0], i)] = my_dict[key] + lst[i]
                keys_to_add.append((key[0], i))
            my_dict[(i, i)] = lst[i]
            keys_to_add.append((i, i))
        keys_list += keys_to_add
    print(my_dict)


largest_seq([1, 0, 3, -8, 4, -2, 3])
