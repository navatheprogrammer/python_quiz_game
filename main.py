print("welcome")



score = 0


awnser1 = input("what language are we using?: ") #python  


if awnser1.lower() == "python":
    print("bravo")
    score += 1

awnser2 = input("what command starts git") #git init

if awnser2.lower() == "git init":
    print("bravo")
    score += 1

    
else:
    print("wrong")


print("your score is", score)