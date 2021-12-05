import math
import random
import numpy


class PermGenerator:
    """
    generator of sample permutation based on a string and the sample percent.
    """

    def __init__(self, perm, sample_percent):
        self.perm = perm
        self.sample_percent = sample_percent
        self.check_repetition()
        self.modulo_jumps_size = self.sample_percent ** -1
        self.num_of_perm = self.find_num_of_perm()

    def __iter__(self):
        """
        generator of a stream based on the sample percent value
        the amount of the  iterations is the amount of permutations
        that needs to be generated based on the sample percent.
        on each iteration the func is choosing between the first number of the current iteration and
        the last based on the jump size that is needed.
        with using floats until the last moment to better the resolution.
        :return: permutation from the sample stream
        """
        for cur_perm in numpy.arange(0, self.num_of_perm, self.modulo_jumps_size):
            chosen_perm = random.randint(int(cur_perm), int(cur_perm + self.modulo_jumps_size) - 1)
            yield self.find_permute(chosen_perm)

    def find_permute(self, perm_id):
        """
        function finds permutation by index ranging from 0 to the amount of the permutations, the logic is if we look
        at the tree of the permutations, on each level we can choose 1 char from  length of the string- level in each
        iteration the perm_id is the deciding factor which char from the perm to take and insert it in the new
        permutation the decision is base on the perm_id modulo length of the current perm. :param perm_id: the number
        of the permutation
        :return: the permutation that correspond to the unique perm_id
        """
        og_perm = self.perm
        new_perm = ""
        while len(og_perm) > 0:
            chosen_char = perm_id % len(og_perm)
            new_perm = new_perm + og_perm[chosen_char]
            perm_id = int(perm_id / len(og_perm))
            og_perm = og_perm.replace(og_perm[chosen_char], "")
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


def check_string_perm(gen):
    """
    (2) checking if a given string is in the sample data
    :param gen: the generator
    :return: if the string is in the sample return true' else false
    """
    check = input("insert string you would like to check:")
    if len(check) != len(gen.perm):
        print("the input isn't the same length as the length of the permutation from the stream")
        return False
    if max([check(c) for c in check]) != 1:
        print("input is invalid, there is a char that repeats itself")
        return False
    for perm in gen:
        if perm == check:
            print("the input is in the sample stream")
            return True
    print("the input isn't in the sample stream")
    return False


def perm_ruuning():
    perm1 = PermGenerator("abc", 1)
    perm2 = PermGenerator("abcd", 0.5)
    perm3 = PermGenerator("abcde", 0.05)
    perm4 = PermGenerator("abcdefg", 0.05)
    print("generator perm 1 is for string: 'abc' and generates sample stream of all the perm")
    print("generator perm 2 is for string: 'abcd' and generates sample stream of 50% of the perm")
    print("generator perm 3 is for string: abcde' and generates sample stream of 5% of the perm")
    print("generator perm 3 is for string: abcdefg' and generates sample stream of 5% of the perm")
    print("for checking  your string with perm1:")
    check_string_perm(perm1)
    print("for checking  your string with perm2:")
    check_string_perm(perm2)
    print("for checking  your string with perm3:")
    check_string_perm(perm3)
    print("for checking  your string with perm4:")
    check_string_perm(perm4)


if __name__ == '__main__':
    perm_ruuning()
