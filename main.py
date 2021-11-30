import math
import random

def find_permute(i, perm):
    new_perm = ""
    while len(perm) > 0:
        j = i % len(perm)
        new_perm = new_perm + perm[j]
        i = int(i / len(perm))
        perm = perm.replace(id[j], "")
    return new_perm

def gen_permute(perm, sample_percent):
    repetition_check(perm)
    num_of_perm = math.factorial(len(perm))
    modolu_jumps_size = int(sample_percent ** -1)
    for iteration in range(0, num_of_perm, modolu_jumps_size):
        cur_perm = iteration + random.randint(0, modolu_jumps_size - 1)
        yield find_permute(cur_perm, perm)

def repetition_check(perm):
    if max([perm.count(c) for c in perm]) != 1:
        raise TypeError("all characters in the string must not repeat")
    return


def checkIfDuplicate(permlist):
    ''' Check if given list contains any duplicates '''
    for perm in permlist:
        if permlist.count(permlist) > 1:
            return perm
    return "all good"

def get_perm_list(perm):
    m = math.factorial(len(id))
    print('there are :', m, " different permutations")
    count = 0
    permlist = []
    for perm in gen_permute(id, 1):
        permlist.append(perm)
        count+=1
    print(count, m)

def check_string_perm(check):
    m = math.factorial(len(check))
    print('there are :', m, " different permutations")
    for perm in gen_permute(check, 1):
        if perm == check:
            return True
    return False
def get_perm():
    check= input("Enter the string you want to check: ")
    check_string_perm(check)
if __name__ == '__main__':
    get_perm()