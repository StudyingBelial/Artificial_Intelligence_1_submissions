from approvedimports import *

def exhaustive_search_4tumblers(puzzle: CombinationProblem) -> list:
    """simple brute-force search method that tries every combination until
    it finds the answer to a 4-digit combination lock puzzle.
    """

    # check that the lock has the expected number of digits
    assert puzzle.numdecisions == 4, "this code only works for 4 digits"

    # create an empty candidate solution
    my_attempt = CandidateSolution()

    # ====> insert your code below here
    #Creating a list of numbers from 0000 to 9999 as str
    guess = [f"{i:04}" for i in range(10000)]

    #Turning the list of number into valid values accepted by CandidateSolution
    guess_list = [[10 if int(j) == 0 else int(j)for j in i] for i in guess]

    for guess in guess_list:
        #print(f"Attempted Guess: {guess}\n")

        try:
            my_attempt.variable_values = guess
            result = puzzle.evaluate(my_attempt.variable_values)

            if (result == 1):
                print("Correct Guess!")
                return guess
        except Exception as e:
            print(f"ERROR: {e}")

    return 0
    # <==== insert your code above here

    # should never get here
    return [-1, -1, -1, -1]

def get_names(namearray: np.ndarray) -> list:
    family_names = []
    # ====> insert your code below here
    for last_names in namearray[:, -6:]:
        family_names.append(''.join(last_names))

    # <==== insert your code above here
    return family_names

def check_sudoku_array(attempt: np.ndarray) -> int:
    tests_passed = 0
    slices = []  # this will be a list of numpy arrays

    # ====> insert your code below here
    if (attempt.shape != (9,9) or attempt.ndim != 2):
        return
    # use assertions to check that the array has 2 dimensions each of size 9
    for row in range(9):
        slices.append(attempt[row,:])
    for column in range(9):
        slices.append(attempt[:,column])
    for i in range(0,9,3):
        for j in range(0,9,3):
            slices.append(attempt[i:i+3, j:j+3])

    ## Remember all the examples of indexing above
    ## and use the append() method to add something to a list

    for slice in slices:  # easiest way to iterate over list
        # print(slice) - useful for debugging?
        print(slice)

        # get number of unique values in slice
        unique = np.unique(slice).shape[0]
        if unique == 9:
            tests_passed += 1
        # increment value of tests_passed as appropriate

    # <==== insert your code above here
    # return count of tests passed
    return tests_passed
