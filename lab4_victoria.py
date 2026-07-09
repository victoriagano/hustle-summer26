# # Ticket 1
# ages = [17, 11, 25, 13, 9]

# # PREDICT: 17, 25, and 13 will get Access granted. 11 and 9 will get Too young.
# for age in ages:
#     if age >= 13:
#         print(f"{age} — Access granted ✅")
#     else:
#         print(f"{age} — Too young ❌")
    
#     # EXPLAIN: The variable age holds one age from the list each time the loop runs.

# # Ticket 2
# # PREDICT: If the user types "no" after the first check, the loop stops after that check.

# keep_checking = "yes"

# while keep_checking == "yes":
#     age = int(input("Enter an age: "))

#     if age >= 13:
#         print(f"{age} — Access granted ✅")
#     else:
#         print(f"{age} — Too young ❌")

#     keep_checking = input("Do you want to check another age? Type yes or no: ")

# # EXPLAIN: A while loop is better here because we do not know ahead of time how many ages the user wants to check.

# # Ticket 3
# # PREDICT: If I forgot the break statement, the loop would keep running forever.

# while True:
#     user_input = input("Enter an age or type stop: ")

#     if user_input == "stop":
#         break

#     age = int(user_input)

#     if age >= 13:
#         print(f"{age} — Access granted ✅")
#     else:
#         print(f"{age} — Too young ❌")

#  # EXPLAIN: Ticket 2 repeats while the answer is yes, but Ticket 3 repeats forever until the user types stop and break ends the loop.

# # Ticket 4
# def can_access(age):
#     if age >= 13:
#         return True
#     else:
#         return False

# # PREDICT: The output is the same as Ticket 1, but the age check happens inside a function now.
# ages = [17, 11, 25, 13, 9]

# for age in ages:
#     if can_access(age):
#         print(f"{age} — Access granted ✅")
#     else:
#         print(f"{age} — Too young ❌")
    
#  # EXPLAIN: A function is better because I can reuse the same age-check code instead of writing the same if/else every time.


# # Ticket 5
# def signup_report(age_list):
#     approved = 0

#     print("--- StreamPass Signup Report ---")

#     for signup_number, age in enumerate(age_list, start=1):
#         if can_access(age):
#             print(f"Signup #{signup_number} | Age {age} — Access granted ✅")
#             approved += 1
#         else:
#             print(f"Signup #{signup_number} | Age {age} — Too young ❌")

#     print(f"Approved: {approved} out of {len(age_list)}")


# # PREDICT:
# # --- StreamPass Signup Report ---
# # Signup #1 | Age 22 — Access granted ✅
# # Signup #2 | Age 10 — Too young ❌
# # Signup #3 | Age 15 — Access granted ✅
# # Signup #4 | Age 8 — Too young ❌
# # Signup #5 | Age 19 — Access granted ✅
# # Signup #6 | Age 13 — Access granted ✅
# # Approved: 4 out of 6

# signups = [22, 10, 15, 8, 19, 13]
# signup_report(signups)
# # EXPLAIN: A function is better because I can reuse the same age-check code instead of writing the same if/else every time.


# # Ticket 5
# def signup_report(age_list):
#     approved = 0

#     print("--- StreamPass Signup Report ---")

#     for signup_number, age in enumerate(age_list, start=1):
#         if can_access(age):
#             print(f"Signup #{signup_number} | Age {age} — Access granted ✅")
#             approved += 1
#         else:
#             print(f"Signup #{signup_number} | Age {age} — Too young ❌")

#     print(f"Approved: {approved} out of {len(age_list)}")


# # PREDICT:
# # --- StreamPass Signup Report ---
# # Signup #1 | Age 22 — Access granted ✅
# # Signup #2 | Age 10 — Too young ❌
# # Signup #3 | Age 15 — Access granted ✅
# # Signup #4 | Age 8 — Too young ❌
# # Signup #5 | Age 19 — Access granted ✅
# # Signup #6 | Age 13 — Access granted ✅
# # Approved: 4 out of 6

# signups = [22, 10, 15, 8, 19, 13]
# signup_report(signups)
# # EXPLAIN: A function is better because I can reuse the same age-check code instead of writing the same if/else every time.


# # Ticket 5
# def signup_report(age_list):
#     approved = 0

#     print("--- StreamPass Signup Report ---")

#     for signup_number, age in enumerate(age_list, start=1):
#         if can_access(age):
#             print(f"Signup #{signup_number} | Age {age} — Access granted ✅")
#             approved += 1
#         else:
#             print(f"Signup #{signup_number} | Age {age} — Too young ❌")

#     print(f"Approved: {approved} out of {len(age_list)}")


# # PREDICT:
# # --- StreamPass Signup Report ---
# # Signup #1 | Age 22 — Access granted ✅
# # Signup #2 | Age 10 — Too young ❌
# # Signup #3 | Age 15 — Access granted ✅
# # Signup #4 | Age 8 — Too young ❌
# # Signup #5 | Age 19 — Access granted ✅
# # Signup #6 | Age 13 — Access granted ✅
# # Approved: 4 out of 6

# signups = [22, 10, 15, 8, 19, 13]
# signup_report(signups)

# # EXPLAIN: I used lists, for loops, while loops, while True, input, int, if/else conditionals, functions, return values, enumerate, a counter variable, and len().