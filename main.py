from question import questoions


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
    