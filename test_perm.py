from permutations import *
import numpy




def test_count_sample_percent():
    """
    checking if the amount for the percent that is generated is the right amount
    :return:
    """
    delta_error=1
    perm_check = "0"
    perm_list = []
    for i in range(1, 8):
        for per in numpy.arange(0.1, 1, 0.05):
            gen = PermGenerator(perm_check, per)
            for perm_gen in gen:
                perm_list.append(perm_gen)
            sample_size = int(math.factorial(len(perm_check)) * per)
            if perm_list:
                if len(perm_list) - delta_error > sample_size or sample_size > len(perm_list) + delta_error:
                    print(perm_check, per)
                    assert False
            else:
                if sample_size != 0:
                    assert False
            del perm_list[:]
        perm_check += str(i)
    assert True


def test_all_perms_unique():
    """
    test for checking if the function that create unique perm per i is correct
    string size from 1 to 10
    :return:
    """
    perm_check = 'a'
    perm_list = []

    for i in range(1,9):
        gen = PermGenerator(perm_check, 1)
        for perm_gen in gen:
            perm_list.append(perm_gen)

        for perm in perm_list:
            if perm_list.count(perm) > 1:
                assert False
        del perm_list[:]
        perm_check += str(i)
    assert True


def test_all_perms_are_other_perms():
    """
    check if all the permutation the generator is providing are indeed a permutation of the origin string
    if they are then when all the generated permutation are sorted then they all are the same string and
    there are n! string of the same permutation
    :return:
    """
    perm_check = "0"
    perm_list = []
    for i in range(1, 8):
        gen = PermGenerator(perm_check, 1)
        for perm_gen in gen:
            perm_list.append(sorted(perm_gen))
        if perm_list.count(sorted(perm_check)) != math.factorial(i):
            assert False
        del perm_list[:]
        perm_check += str(i)
    assert True
