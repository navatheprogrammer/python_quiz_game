from question import questoions




print("welcome")



score = 0
for  item in questoions:
    awnser = input(item["questoion"])
    if awnser.lower() == item["awnser"]:
        print("correct")
        score += 1
    else:
        print("wrong")

print("your score is", score)