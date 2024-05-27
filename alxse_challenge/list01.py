#!/usr/bin/python3

scores = [79, 68, 98, 55]

for score in scores:
    print(f"Before: {score}")
    # for any score less than 90, add 10 marks
    if score < 90:
        score += 10

    print(f"After: {score}")