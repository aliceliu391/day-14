from art import logo
from art import vs
from game_data import data
import random
from replit import clear

def pick_number():
    """picks a random list index"""
    return random.randint(0, len(data) - 1)

def show_details(letter, index):
    """shows the details for a person"""
    if letter == "A":
        print(f"Compare A: {data[index]['name']}, a {data[index]['description']} from {data[index]['country']}.")
    else:
        print(f"Against B: {data[index]['name']}, a {data[index]['description']} from {data[index]['country']}.")

def get_followers(index):
    """gets follower count for someone"""
    return data[index]['follower_count']

result = {
    "bad": "You got under 4.. yikes. You suck!",
    "ok": "Well, you tried. A+ (B) for effort?",
    "good": "You've got what it takes! Get on the grind."

}

right = True
score = 0
first = 0
second = 0

while right:
    clear()
    print(logo)
    
    if score != 0:
        print(f"You're right! Current score: {score}")        
    
    #random list indexes
    if score == 0:
        first = pick_number()
        second = pick_number()
    else:
        first = second
        second = pick_number()
        
    #follower counts
    first_following = get_followers(first)
    second_following = get_followers(second)
    if first_following > second_following:
        greatest = "A"
    elif second_following > first_following:
        greatest = "B"
    else:
        greatest = "C" #they equal, any answer is correct

    print(first_following)
    print(second_following)
    
    #shows details for the comparison
    show_details(letter = "A", index = first)
    print(vs)
    show_details(letter = "B", index = second)
    
    #ask for a choice
    ans = input("Who has more followers? Type 'A' or 'B': ").upper()

    if ans == greatest or ans == "C":
        score += 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        right = False

if score < 4:
    print(result["bad"])
elif score < 6:
    print(result["ok"])
else:
    print(result["good"])