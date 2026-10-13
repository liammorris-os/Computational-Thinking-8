dog_points = 0
cat_points = 0
other_animals = 0
answer1 = input("Would you rather A, Take a nap, B, run outside, or C, go hurdle jumping? ")
if answer1 == "A" or answer1 == "a":
    cat_points += 2
elif answer1 == "B" or answer1 == "b":
    dog_points += 1
elif answer1 == "C" or answer1 == "c":
    other_animals += 1

answer2 = input("Would you rather A, play with a punching bag, B, Hunt in the woods, or C, eat food? ")
if answer2 == "A" or answer2 == "a":
    dog_points += 1
elif answer2 == "B" or answer2 == "b":
    cat_points += 2
elif answer2 == "C" or answer2 == "c":
    other_animals += 1
    dog_points += 1
    cat_points += 1

answer3 = input("Would you rather A, go for a run, B, sit down and read, or C, find a friend to hang out with ")
if answer3 == "A" or answer3 == "a":
    dog_points += 1
elif answer3 == "B" or answer3 == "b":
    cat_points += 1
elif answer3 == "C" or answer3 == "c":
    other_animals += 1

answer4 = input("Would you rather A, Yell outside, B, Lay down in bed, or C, go play a sport ")
if answer4 == "A" or answer4 == "a":
    dog_points += 1
elif answer4 == "B" or answer4 == "b":
    cat_points += 1
elif answer4 == "C" or answer4 == "c":
    other_animals += 1

answer5 = input("Would you rather A, be outside, B, play on a tower, or C, Drink water")
if answer5 == "A" or answer5 == "a":
    dog_points += 1
elif answer5 == "B" or answer5 == "b":
    cat_points += 2
elif answer5 == "C" or answer5 == "c":
    other_animals += 1
    dog_points += 1
    cat_points += 1

if dog_points > cat_points and dog_points > other_animals:
# you get this answer by getting the most dog points
    print("You are a dog!")
elif cat_points > dog_points and cat_points > other_animals:
# you get this answer by getting the most cat points
    print("You are a cat!")
elif other_animals > cat_points and other_animals > dog_points:
# you get this ending by getting the most "other animal" points
    print("You are a animal that is not a cat or a dog!")