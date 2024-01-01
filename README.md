# Permutations Generator

This Python project includes a permutation generator (`PermGenerator`) capable of creating sample permutations based on a given string and a specified sample percentage. The main script (`main.py`) demonstrates the usage of the generator with two examples and includes a function to check if a given string is in the generated sample stream.

## `permutations.py`

The main script includes the following functionalities:

- `PermGenerator`: A class that generates permutations based on a string and a sample percentage. It uses a generator function to produce a stream of permutations.
- `check_string_perm`: A function that takes a generator and checks if a given string is in the sample stream. It also validates the input string against the length and character uniqueness of the generator's string.
- `perm_running`: A function that demonstrates the usage of `PermGenerator` with two examples, showcasing a sample stream of all permutations and a sample stream with 50% of the permutations.

To run the example, execute the `main.py` script.

## `test_perm.py`

The `test_perm.py` script contains unit tests for the `PermGenerator` class. The tests include:

- `test_count_sample_percent`: Checks if the number of permutations generated matches the expected sample size for different string lengths and sample percentages.
- `test_all_perms_unique`: Ensures that all generated permutations are unique for string sizes ranging from 1 to 10.
- `test_all_perms_are_other_perms`: Verifies if all generated permutations are valid permutations of the original string.

To run the tests, execute the `test.py` script.
