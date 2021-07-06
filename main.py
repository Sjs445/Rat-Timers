import time
from msvcrt import getch

# Store the associated key, its start time, total time, and whether it was
# pressed or not.
# {'b':
#      {'total_time': float,
#       'start_time': float,
#       'key_pressed': bool
#       }
# }
key_dict = {}


def main():
    get_actions()
    begin_work()

    print("\n\nTotal time for individual actions")
    for key in key_dict:
        print(f"{chr(key)}", "{:.6g}".format(key_dict[key]['total_time']))

    input()


def get_actions():
    print("Enter as many keys as you want to represent an action (ESC to finish)\n")
    while True:
        key = ord(getch())

        if key == 27:  # ESC
            break

        key_dict[key] = {
            'total_time': 0,
            'start_time': 0,
            'key_pressed': False
            }
        print("Added", chr(key))


def print_pressed_keys():
    """
    Prints any active timers
    """
    print("Active timers:")
    print("==================")
    for key in key_dict:
        if key_dict[key]['key_pressed']:
            print(chr(key))
    print("==================")


def is_timing():
    """
    Checks if there are active keys
    """
    for key in key_dict:
        if key_dict[key]['key_pressed']:
            return False

    return True


def begin_work():
    print("""When ready, press the key you want and the timer will begin for that action.
             When you're done, press the same key to stop the timer for that action.
             Press ESC to quit.""")
    print("You can also press 9 to check if there are active timers.")
    while True:
        key = ord(getch())

        if key == 27 and is_timing():
            break
        elif key == 27 and not is_timing():
            print("You still have these timers active")
            print_pressed_keys()
            continue
        elif key == 57:
            print_pressed_keys()
            continue

        if key in key_dict and not key_dict[key]['key_pressed']:
            # If the key is being pressed for the first time,
            # we get the start time and set our timer to start.
            start_time = time.time()
            key_dict[key]['start_time'] = start_time
            key_dict[key]['key_pressed'] = True
        elif key in key_dict and key_dict[key]['key_pressed']:
            # If the key is being pressed for a second time,
            # we stop our timer and calculate the total time it
            # took in between presses.
            start_time = key_dict[key]['start_time']
            end_time = time.time()
            key_dict[key]['total_time'] += end_time - start_time

            # Print the time, but format it to 6 sig figs
            print(f"\nTime for {chr(key)}", "{:.6g}".format(key_dict[key]['total_time']))

            # Set our timer to False to stop timing
            key_dict[key]['key_pressed'] = False
        else:
            print(f"{chr(key)} was not added at the start!")


if __name__ == "__main__":
    main()
