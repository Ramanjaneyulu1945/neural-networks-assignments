score=int(input("Please enter your score:"))
print("Your score is",score)
if score >= 90 and score <= 100:
    print("Your Grade is A")
elif score >= 80 and score <= 89:
    print("Your Grade is B")
elif score >= 70 and score <= 79:
    print("Your Grade is C")
elif score >= 60 and score <= 69:
    print("Your Grade is D")
else:
    print("Your Grade is F")

