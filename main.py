import math
import random


def find_permute(i, perm):
    new_perm = ""
    while len(perm) > 0:
        j = i % len(perm)
        new_perm = new_perm + perm[j]
        i = int(i / len(perm))
        perm = perm.replace(perm[j], "")
    return new_perm


def gen_permute(perm, sample_percent):
    repetition_check(perm)
    num_of_perm = math.factorial(len(perm))
    modulo_jumps_size = int(sample_percent ** -1)
    for iteration in range(0, num_of_perm, modulo_jumps_size):
        cur_perm = iteration + random.randint(0, modulo_jumps_size - 1)
        yield find_permute(cur_perm, perm)


def repetition_check(perm):
    if max([perm.count(c) for c in perm]) != 1:
        raise TypeError("all characters in the string must not repeat")
    return


def check_if_duplicate(perm_list):
    # Check if given list contains any duplicates
    for perm in perm_list:
        if perm_list.count(perm_list) > 1:
            return perm
    return "all good"


def get_perm_list(perm):
    m = math.factorial(len(perm))
    print('there are :', m, " different permutations")
    count = 0
    perm_list = []
    for perm in gen_permute(perm, 1):
        perm_list.append(perm)
        count += 1
    print(count, m)


def check_string_perm(check):
    m = math.factorial(len(check))
    print('there are :', m, " different permutations")
    for perm in gen_permute(check, 0.1):
        if perm == check:
            return True
    return False


def get_perm():
    check = input("Enter the string you want to check: ")
    if check_string_perm(check):
        print("found the string in the sample")
    else:
        print ("didn't found the string in the sample")
def user_input():
    while True:
        get_perm()

if __name__ == '__main__':
    user_input()
