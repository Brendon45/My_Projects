#!/usr/bin/python3

import time

def countdown_and_greet():
    for seconds in range(10, 0, -1):
        print(f"Countdown: {seconds}")
        time.sleep(1)
    print("Happy New Month!")

if __name__ == "__main__":
    countdown_and_greet()
