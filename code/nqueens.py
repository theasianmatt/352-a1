import random
import time
# create starting spots for queens
# start w one queen per column, all in first row
max_steps = 100

def print_board(queens, board_size):
    for i in range(board_size):
        print("X",end='')
    print()
    for row in range(board_size):
        for column in range(board_size):
            occupied=False
            for i, q in enumerate(queens):
                if i == column and q == row +1:
                    print(validate(queens,i),end='')
                    occupied = True

            if not occupied:
                print("_",end='')
        print()

def generate_start_board(board_size):
    start_positions = []
    for j in range(board_size):
        # uncomment for random start
        start_positions.append(random.randint(1,board_size))
        #start_positions.append(j+1)
    return start_positions


# returns number of conflicts
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

# Count errors for all queens 
def count_errors(queens):
    errors = []
    total = 0
    for i in range(len(queens)):
        e = validate(queens, i)
        total += e
        errors.append((i, e))
    errors.sort(key=lambda tup: tup[1], reverse=True)
    # returns a random list of the worst queens
    # uncomment for random
    #random.shuffle(errors)
    return (total, errors)

# Find the least conflicted square to move
def get_best_pos(queens,q,board_size):
    tempq = queens.copy()
    lowest = 1000000000000
    lowest_i = -1
    for i in range(board_size):
        tempq[q] = i + 1
        e = validate(tempq, q)
        if e < lowest:
            lowest = e
            lowest_i = i + 1
    return lowest_i

# Implement a solver that returns a list of queen's locations
#  - Make sure the list is the right length, and uses the numbers from 0 .. BOARD_SIZE-1

def solve(board_size):
    global max_steps
    start = time.time()
    # List of n queens
    # min-conflics alg
    tries = 0
    while time.time()-start < 1800:
        tries+=1
        queens = generate_start_board(board_size)
        error_queens = []
        for count in range(max_steps):
            errors, temp= count_errors(queens)
            if len(error_queens) == 0 or temp[0][1] < error_queens[0][1]:
                #    print("{} {} {}".format(count,error_queens,temp))
                error_queens = []
                for x in temp:
                    if x[1] == temp[0][1]:
                        error_queens.append(x)
                    else:
                        break
                random.shuffle(error_queens)
            if errors > 0:
                # get the worst queen
                worst = error_queens.pop()
                queens[worst[0]] = get_best_pos(queens,worst[0],board_size)
                #print_board(queens,board_size)
            else:
                print("SOLVED {}-queen problem in {} steps with {} seconds on try {}".format(board_size,count, time.strftime("%H:%M:%S", time.gmtime(time.time() - start)),tries))
                #print_board(queens,board_size)
                return queens

    # should never get here unless fail
    print("FAILED {}-queen problem in {} steps with {} seconds on try {}".format(board_size,count, time.strftime("%H:%M:%S", time.gmtime(time.time() - start)),tries))
    #print_board(queens,board_size)
    return queens


if __name__ == "__main__":
    print(solve(4));
