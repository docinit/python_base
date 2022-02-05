import itertools

def generator(input_list):
    z = 0
    for i in itertools.cycle(input_list):
        input_list[input_list.index(i)] = i**2
        summa = sum(input_list)
        input_list.extend(input_list)
        if summa>=1e10:
            result_list = input_list
            z+=1
            break
        z += 1
    return z,summa,result_list