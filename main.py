# This is a sample Python script.
import math
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def find_permute(i, id):
    m = math.factorial(len(id))
    flag = m / 2
    new_id = ""
    while len(id) > 2:
        if i < len(id):
            j = i
        else:
            j = i % len(id)
        new_id = new_id + id[j]
        id = id.replace(id[j], "")
    if (i < flag):
        j = 1
    else:
        j = 0
    new_id = new_id + id[j]
    id = id.replace(id[j], "")
    new_id = new_id + id
    return new_id


def gen_permute(perm, sample_percent):
 #   if not isPermUnique(perm):
  #      return ""
    num_of_perm = math.factorial(len(perm))
    modolu_jumps_size = int(sample_percent**-1)
    for iteration in range(0, num_of_perm, modolu_jumps_size):
        cur_perm = iteration + random.randint(0, modolu_jumps_size - 1)
        yield find_permute(cur_perm, perm)


def isPermUnique(perm):
    # Counting frequency
    return (max([perm.count(c) for c in perm]) == 1)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    id = "1234"
    m = math.factorial(len(id))
    print('there are :', m)
    # permlist =gen_permute("1234",0.5)
    # i = 0
    # while i < m:
    #     print(permlist)
    #     i = i + 1
    for perm in gen_permute("1234", 0.5):
        print(perm)
