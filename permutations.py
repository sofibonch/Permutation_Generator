import math
import random


class PermGenerator:
    """
    generator of sample permutation based on a string and the sample percent.
    """

    def __init__(self, perm, sample_percent):
        self.perm = perm
        self.sample_percent = sample_percent
        self.check_repetition()
        self.check_sample_percent()
        self.modulo_jumps_size = int(self.sample_percent ** -1)
        self.num_of_perm = self.find_num_of_perm()
        #@property
    def __iter__(self):
        if self.sample_percent*len(self.perm)>=1:
            for iteration in range(0, self.num_of_perm, self.modulo_jumps_size):
                cur_perm = iteration + random.randint(0, self.modulo_jumps_size - 1)
                yield self.find_permute(cur_perm)
        else:
            yield ""
    def check_sample_percent(self):
        if self.sample_percent <= 0 and self.sample_percent > 1:
            raise ValueError("the sample percent must be more than 0 and less or equal to 1")
        return

    def find_permute(self, perm_id):
        """
        function finds permutation by index ranging from 0 to the amount of the permutations, the logic is if we look
        at the tree of the permutations, on each level we can choose 1 char from  length of the string- level in each
        iteration the perm_id is the deciding factor which char from the perm to take and insert it in the new
        permutation the decision is base on the perm_id modulo length of the current perm. :param perm_id: the number
        of the permutation
        :return: the permutetion that correspond to the i
        """
        og_perm = self.perm
        new_perm = ""
        while len(og_perm) > 0:
            chosen_char = perm_id % len(og_perm)
            new_perm = new_perm + og_perm[chosen_char]
            perm_id = int(perm_id / len(og_perm))
            og_perm = og_perm.replace(og_perm[chosen_char], "")
        print(new_perm)
        return new_perm

    def check_repetition(self):
        """
        checks if the the given string for the generator is valid.
        :return: raises an error if the string is incorrect.
        """
        if max([self.perm.count(c) for c in self.perm]) != 1:
            raise TypeError("all characters in the string must not repeat")
        return

    def find_num_of_perm(self):
        if len(self.perm) == 0:
            raise TypeError("empty string")
        else:
            return math.factorial(len(self.perm))

# def check_if_duplicate(perm_list):
#     # Check if given list contains any duplicates
#     for perm in perm_list:
#         if perm_list.count(perm_list) > 1:
#             return perm
#     return "all good"


# def get_perm_list(perm):
#     m = math.factorial(len(perm))
#     print('there are :', m, " different permutations")
#     count = 0
#     perm_list = []
#     for rand_perm in gen_permute(perm, 1):
#         perm_list.append(rand_perm)
#         count += 1
#
#     print(count, m)


def check_string_perm(gen):
    """
    (2) checking if a given string is in the sample data
    :param gen: the generator
    :param check:user input that the user want to check if it's in the permutation sample
    :return: if the string is in the sample return true' else false
    """
    check = input("insert string you would like to check:")
    m = math.factorial(len(check))
    print('there are :', m, " different permutations")
    for perm in gen:
        if perm == check:
            print("the input is in the sample stream")
            return True
    print("the input isn't in the sample stream")
    return False


def get_perm():
    check = input("Enter the string you want to check: ")
    if check_string_perm(check):
        print("found the string in the sample")
    else:
        print("didn't found the string in the sample")


if __name__ == '__main__':
    perm1 = PermGenerator("abcde", 1)
    check_string_perm(perm1)
