

import os
from dotenv import load_dotenv
from question import questoions




load_dotenv()
admin_pass = os.getenv("QUIZ_ADMIN_PASSWORD")
open_admin = input("do you want to open admin mode? yes/no: ")
if open_admin.lower () == "yes":
    entered_password = input("enter admin password pls: ")
    if  entered_password == admin_pass:
        print("admin hi....")
    else:
        print("wrong password")

name = input("what is your name: ")

print("welcome")



score = 0
for  item in questoions:
    awnser = input(item["question"])
    if awnser.lower() == item["awnser"]:
        print("correct")
        score += 1
    else:
        print("wrong")

print("your score is", score, "out of", len(questoions))

if score == len(questoions):
    print("exelent job", name)


elif score >=2:
    print("good job", name)

else:
    print("keep practicing", name)



with open("result.txt", "a") as file:
    file.write(f"{name} - {score}/{len(questoions)}\n")
