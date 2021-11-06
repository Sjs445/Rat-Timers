# Rat Timers

## About

This console app was designed specifically to time any actions an experimental rat might do by using keyboard presses. Each keyboard press denotes an action.

## Requirements

Current requirements is just Python3.

If you are on Mac/Linux you will need to run the install.sh file.

## Download and Run

```
git clone https://github.com/Sjs445/Rat-Timers.git
```

```
cd Rat-Timers
```

```
python3 main.py
```

Or click the green code button and then click Download ZIP. Extract the files and then double click the main.py file or the run.sh file.


## How it works

The program first asks you to input any number of keys to represent an action you will be timing.

```
Enter as many keys as you want to represent an action (ESC to finish)

Added b
Added t
```

In the example above we pressed 'b' and then 't' to denote we want to time how long the rat will be in the 'box' and how long the rat will be 'touching' things.

After you press escape you can begin timing.

```
1. Press the key you want and the timer will begin for that action.
2. Press the same key to stop the timer for that action.
3. Press the SPACE key to increment a counter.
4. Press ESC to quit.
5. Press 9 to check if there are active timers.
```

Now if you press b or t you will begin timing those actions. Press b or t a second time to stop timing those actions.

```
Started timing for b
Started timing for t

Time for t 5.21666

Time for b 7.7127
```

You can also press SPACE to increment a counter:
```
Counter increased: 1
Counter increased: 2
Counter increased: 3
Counter increased: 4
```

By pressing escape you will end the program and it will give you the total time recorded for each action.

```
Total time for individual actions
b 7.7127
t 5.21666
Counter:  4
```

## Author

Shane Spangenberg
