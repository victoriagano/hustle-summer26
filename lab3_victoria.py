
# Victoria Gano |Lab 3| Intro to Python

# Ticket 1
username = "vicccc"
# PREDICT: 6
print(len(username))
# EXPLAIN: Yes, len() counts every character in the string, including symbols if there are any

# Ticket 2
print(username[0])
print(username[len(username) - 1])
# PREDICT: v and c
#EXPLAIN: The last index is len(username)-1 because Python starts counting at 0python3 lab3_victoria.py

# Ticket 3
print("Welcome to Loop, @" + username + "!")
print(f"Welcome to Loop, @{username}!")
#PREDICT: Yes, both lines will look identical.
#EXPLAIN: The f-string method felt easier because it was cleaner without the extra + signs 

# Ticket 4 
#username[0] = "X"
# TypeError: 'str' object does not support item assignment
username = "vicccc"
print(username.upper())
#PREDICT: I think the program will crash because strings cannot be changed by index
#EXPLAIN:  A string is immutable, which means you cannot change individual characters after it is created. You have to make a new string instead.

# Ticket 5
feed = ["Life's a dream", "Finished my homework", "Ready for the weekend"]
print(len(feed))
print(feed[0])

# Ticket 6
feed.append("Live Laugh Love")
print(feed)
#PREDICT: The new fourth post will be at index 3
#EXPLAIN: The fourth post is at index 3 because lists start counting at 0

# Ticket 7
feed.pop(0)
feed.sort()
print(feed)
#PREDICT: "Life is a dream" will be removed, and the remaining posts will be in alphabetical order.
#EXPLAIN: I used pop() to remove the first post from the list, and sort() to put the remaining posts in alphabetical order.

# Ticket 8
profile = {
    "username": "vicccc",
    "followers": 200,
    "verified": True
}
print(profile["followers"])
# profile[0]
# KeyError: 0 
# PREDICT: The follower count 200 will print, and I think profile[0] will cause an error.
# EXPLAIN: Dictionaries use keys like "username" and "followers" to find values instead of number indexes.

# Ticket 9
profile["followers"] = profile["followers"] + 50
profile["bio"] = "Wow this is awesome"

print(profile)
print(profile.get("age"))
#PREDICT: It will print None 
#EXPLAIN: .get() is safer because it returns None if the key does not exist instead of causing an error.

# Ticket 10 
print(f"@{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]}")
# PREDICT: @vicccc has 250 followers and 3 posts. Top post: Can't wait for summer
# EXPLAIN: I used a dictionary (profile), a list (feed), a string, and the len() function to build this line.