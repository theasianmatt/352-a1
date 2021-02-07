import random
# create starting spots for queens
# start w one queen per column, all in first row
max_steps = 100000000000

def print_board(queens, board_size):
    for i in range(board_size):
        print("X",end='')
    print()
    for row in range(board_size):
        for column in range(board_size):
            occupied=False
            for i, q in enumerate(queens):
                if i == column and q == row +1:
                    print("Q",end='')
                    occupied = True

            if not occupied:
                print("_",end='')
        print()

def generate_start_board(board_size):
    start_positions = []
    for j in range(board_size+1):
        # print(startPositions)
        start_positions.append(j)
        #print(start_positions)
        # Do something with list of starting positions
        #print(count_errors(start_positions))
    return start_positions


# Returns false if not valid, true if valid
def validate(queens, i):
    errors = 0

    q = queens[i]
    for j, q2 in enumerate(queens):
        if i != j:
            # Same row (columns are always different)
            if q == q2:
                errors += 1
            # Figure out diagonal
            # If the difference between the two coordiates have the same
            # absolute x and y value, then they are on the diagonal
            elif abs(i - j) == abs(q - q2):
                errors += 1
    return errors


def count_errors(queens):
    errors = []
    total = 0
    for i in range(len(queens)):
        e = validate(queens, i)
        total += e
        errors.append((i, e))
    errors.sort(key=lambda tup: tup[1], reverse=True)
    return (total, errors)


# Implement a solver that returns a list of queen's locations
#  - Make sure the list is the right length, and uses the numbers from 0 .. BOARD_SIZE-1

def solve(board_size):
    global max_steps
    # List of n queens
    queens = generate_start_board(board_size)
    for count in range(max_steps):
        errors, error_queens = count_errors(queens)
        if errors > 0:
            # get the worst queen
            worst = error_queens.pop()
            # do something
            # min conflict
            # take the queen with the most conflicts (first queen in error list)
            # move it to the postition with the least conflicts (figure this out)
            tempq = queens.copy()
            lowest = 1000000000000
            lowest_i = -1
            for i in range(board_size):
                tempq[worst[0]] = i + 1
                e = validate(tempq, worst[0])
                if e < lowest:
                    lowest = e
                    lowest_i = i
                #print_board(tempq,board_size)
                print("Loop {} errors: {} e: {}".format(count,errors,e))
            print("Lowest {} lowest i {}".format(lowest,lowest_i))
            print(error_queens)
            queens[error_queens[0][0]] = lowest_i+1
            print_board(queens,board_size)
        else:
            return queens

    # should never get here unless fail
    print("FAILED")
    return queens


if __name__ == "__main__":
    print(count_errors([3,1,4,2]))
    print(count_errors([1,1,1,2]))
