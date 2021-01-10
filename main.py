# variables
array = []
goal = 0


# starts and ends the game
def start_game():
    while True:
        val = input("Start binary search game? (y =yes, n = no): ").lower().strip()
        if val == 'y':
            array_gen()
            binary_search()
            start_game()
        elif val == 'n':
            print("Thanks for playing")
            exit()
        else:
            print("Please enter a valid input")


# generates the array and the goal number
def array_gen():
    array_start = int(input("Please enter number for array start: "))
    array_end = int(input("Please enter number for array end: "))
    global array, goal
    array = list(range(array_start, array_end + 1))
    while goal < array_start or goal > array_end:
        goal = int(input("Please enter number for algorithm to search for: "))


# the actual binary search
def binary_search(bs_array=None, bs_goal=None):
    if bs_array is None:
        bs_array = array
    if bs_goal is None:
        bs_goal = goal
    start = 0
    end = len(bs_array) - 1
    rounds = 1
    while start <= end:
        mid = start + (end - start) // 2
        mid_val = bs_array[mid]
        if mid_val == bs_goal:
            print(f"Target value {mid_val} found in {rounds} cycles")
            break
        elif bs_goal < mid_val:
            rounds += 1
            end = mid - 1
        else:
            rounds += 1
            start = mid + 1


if __name__ == "__main__":
    start_game()
