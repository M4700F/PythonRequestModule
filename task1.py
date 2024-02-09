"""
    The main idea is we take a line from users.csv and then choose the first 3 letters and
    store them,
    then take a line from pass.csv and choose the last 4 letters and store them.
    Then we concatenate them and write in keyword.txt
"""

# first we have to open the users.csv and pass.csv in read mode

# fileusers =   open("users.csv", "r")
# filepass  =   open("pass.csv", "r")
# filekeyword = open("keywords.txt", "w")

# lineusers = fileusers.readline().strip()
# linepass  = filepass.readline().strip()

# while lineusers and linepass:
    
#     users = lineusers[:3]
#     password = linepass[-4:]

# # here I faced a problem. And the problem is very interesting. 
# # When I execute the program, the output for pass is showing only the last three characters 
# # even though I wrote -4. Later I realize that after searching in the net that for the last
# # 4 characters, the newline character is also included that's not what I want. That's why 
# # I use strip() command. This will discard any leading and trailing newline characters. Amazing!

#     # print(users)
#     # print(password)

#     keyword = users + password + "\n"
#     # print(keyword)

#     filekeyword.write(keyword)

#     lineusers = fileusers.readline().strip()
#     linepass  = filepass.readline().strip()

# fileusers.close()
# filepass.close()
# filekeyword.close()

# fileusers = open("users.csv", "r")
# filepass = open("pass.csv", "r")
# filekeyword = open("keywords.txt", "w")

# users_lines = fileusers.readlines()

# for lineusers in users_lines:
#     lineusers = lineusers.strip()

#     filepass.seek(0)  # Reset pass.csv to the beginning
#     for linepass in filepass:
#         linepass = linepass.strip()

#         users = lineusers[:3]

#         password = linepass[-4:]

#         keyword = users + password + "\n"

#         filekeyword.write(keyword)

# fileusers.close()
# filepass.close()
# filekeyword.close()

import sys

def generate_keywords(users_file, pass_file):
    with open(users_file, "r") as fileusers, open(pass_file, "r") as filepass, open("keywords.txt", "w") as filekeyword:
        users_lines = fileusers.readlines()

        for lineusers in users_lines:
            lineusers = lineusers.strip()

            filepass.seek(0)  # Reset pass.csv to the beginning
            for linepass in filepass:
                linepass = linepass.strip()

                users = lineusers[:3]
                password = linepass[-4:]
                keyword = users + password + "\n"

                filekeyword.write(keyword)

users_file = sys.argv[1]
pass_file = sys.argv[2]

generate_keywords(users_file, pass_file)
