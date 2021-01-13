# starts and ends the game
def start_game():
    while True:
        val = input("Start binary search game? (y =yes, n = no): ").lower().strip()
        if val == 'y':
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
    array = list(range(array_start, array_end + 1))
    return array


# the actual binary search
def binary_search():
    bs_array = array_gen()
    print("Think of a number within the array")
    start = 0
    end = len(bs_array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        mid_val = bs_array[mid]
        print(f"Is this your number: {mid_val}?")
        high_low = input("Type y for yes, h for higher, or l for lower: ").lower().strip()
        if high_low == 'y':
            print(f"Target value {mid_val} found.")
            break
        elif high_low == "l":
            end = mid - 1
        elif high_low == "h":
            start = mid + 1
        else:
            print("Please enster valid input")


if __name__ == "__main__":
    start_game()
