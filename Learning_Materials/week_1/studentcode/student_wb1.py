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
