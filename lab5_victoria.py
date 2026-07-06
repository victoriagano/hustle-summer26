# ============================================================
# LAB 5 - WEEK 5 : The VibeCheck Bug Hunt
# ============================================================
# Name: Victoria
#
# This file is BROKEN on purpose. There are 8 bugs.
# ============================================================


# ------------------------------------------------------------
# PART 1 - A function that greets a user
# ------------------------------------------------------------

def send_vibe():
    print("VibeCheck says: good energy only")


def welcome_user():
    print("Welcome to VibeCheck!")


# ------------------------------------------------------------
# PART 2 - A function that uses a variable
# ------------------------------------------------------------

def show_mood():
    mood = "hyped"
    print(f"Today's mood is {mood}")


# ------------------------------------------------------------
# PART 3 - A function with parameters
# ------------------------------------------------------------

def make_shoutout(name, mood):
    return f"{name} is feeling {mood} today!"


# ------------------------------------------------------------
# PART 4 - A function that counts hype points
# ------------------------------------------------------------

def count_hype(likes, shares):
    total = likes + shares
    return total


# ============================================================
# RUNNING THE CODE - do not move these calls above the
# functions they use
# ============================================================

send_vibe()
welcome_user()
show_mood()

print(make_shoutout("Jordan", "creative"))
print(make_shoutout("Alex", "chill"))

print(count_hype(10, 5))


def final_message():
    print("Thanks for using VibeCheck!")


final_message()