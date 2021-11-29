# This is a sample Python script.
import math
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def find_permute(i, id):
    m = math.factorial(len(id))
    flag= m/2
    new_id = ""
    while len(id) > 2:
        if i < len(id):
            j = i
        else:
            j = i% len(id)
        new_id = new_id + id[j]
        id = id.replace(id[j], "")
    if(i<flag):
        j = 1
    else:
        j=0
    new_id = new_id + id[j]
    id = id.replace(id[j], "")
    new_id = new_id + id
    print(new_id)

def gen_permunte (perm,sample_percent):
    num_of_perm = (len(perm))
    num_of_percent=int(num_of_perm*sample_percent)

def isUniqueChars(string):
    # Counting frequency
    return (max([string.count(c) for c in string]) == 1)



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    id= "12345"
    m = math.factorial(len(id))
    print('there are :',m)
    i = 0
    while i < m:
        if(i%len(id) ==0):
            print(" \n")
        #print(i)
        find_permute(i,id)
        i = i + 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
