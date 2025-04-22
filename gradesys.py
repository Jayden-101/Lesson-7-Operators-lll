print("Enter Marks Obtained in 5 Subjects:")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=91 and avg<=100:
    print("your grade is A+")
if avg>=81 and avg<=91:
    print("your grade is A-")
if avg>=71 and avg<=81:
    print("your grade is B+")
if avg>=61 and avg<=71:
    print("your grade is B-")
if avg>=51 and avg<=61:
    print("your grade is C+")
if avg>=41 and avg<=51:
    print("your grade is C-")
if avg>=31 and avg<=41:
    print("your grade is D")
if avg>=21 and avg<=31:
    print("your grade is E+")
if avg>=11 and avg<=21:
    print("your grade is E-")
if avg>=1 and avg<=11:
    print("your grade is F")
