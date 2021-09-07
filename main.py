#!/usr/bin/env python3
import time
import os
import sys

# Do an initial OS check for imports
OPERATING_SYS = os.name

if OPERATING_SYS == 'nt':
    from msvcrt import getch
elif OPERATING_SYS == 'posix':
    from readchar import readchar
else:
    print("Your OS is not supported", file=sys.stderr)
    sys.exit(1)


def determine_read():
    """
    returns the correct read key method to use based on the OS.
    """
    if os.name == "nt":
        return ord(getch())
    elif os.name == "posix":
        return ord(readchar())


# Store the associated key, its start time, total time, and whether it was
# pressed or not.
# {'key':
#      {'total_time': float,
#       'start_time': float,
#       'key_pressed': bool
#       }
# }
key_dict = {}
space_counter = 0


def main():
    """
    Main execution of the program.
    """
    get_actions()
    begin_timing()

    print("\n\nTotal time for individual actions")
    for key in key_dict:
        print(f"{chr(key)}", "{:.6g}".format(key_dict[key]['total_time']))
    print("Counter: ", space_counter)

    print("Press ENTER to run again OR any other key to quit...")
    key = determine_read()
    
    if key == 13:  # ENTER KEY
        key_dict.clear()
        print("\n")
        main()


def get_actions():
    """
    Retrieve keys through input to represent timers.
    """
    print("Enter as many keys as you want to represent an action (ESC to finish)\n")
    while True:
        key = determine_read()

        if key == 27:  # ESC
            if not key_dict:
                print("You haven't added any keys yet.")
                continue
            break
        elif key == 32:  # SPACE
            print("Can not add SPACE key as a timer because that key is reserved for counting.\n")
            continue

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
    print("==================")
    print("Active timers:")
    print("==================")
    for key in key_dict:
        if key_dict[key]['key_pressed']:
            print(chr(key))
    print("==================")
    print("Counter: ", space_counter)
    print("==================")


def is_timing():
    """
    Checks if there are active keys
    """
    for key in key_dict:
        if key_dict[key]['key_pressed']:
            return False

    return True


def begin_timing():
    """
    The timer portion of the program.
    Uses the difference in time.time() to calculate time in between presses.
    """
    global space_counter
    print("""\n1. Press the key you want and the timer will begin for that action.
2. Press the same key to stop the timer for that action.
3. Press the SPACE key to increment a timer.
4. Press ESC to quit.""")
    print("5. Press 9 to check if there are active timers.\n")
    while True:
        key = determine_read()

        if key == 27 and is_timing():
            break
        elif key == 27 and not is_timing():
            print("You still have these timers active")
            print_pressed_keys()
            continue
        elif key == 57:
            print_pressed_keys()
            continue
        elif key == 32:  # SPACE KEY
            space_counter += 1
            print("Counter increased:", space_counter)
            continue

        if key in key_dict and not key_dict[key]['key_pressed']:
            # If the key is being pressed for the first time,
            # we get the start time and set our timer to start.
            start_time = time.time()

            key_dict[key]['start_time'] = start_time
            key_dict[key]['key_pressed'] = True

            print("Started timing for", chr(key))
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
            print(f"{chr(key)} is an invalid action!")


if __name__ == "__main__":
    main()
