age = int(input("enter your age?"))
if (age<18):
    print("You are not an adult.")
    if (age>=13):
        print("You are a teenager.")
elif (age<65):
    print("You are not an adult.")
else:
    print("You are senior citizen.")


mark = int(input("enter your mark?"))
if (100>=mark>=70):
    print("A")
elif (mark>=55):
    print("B")
elif (mark>=40):
    print("C")
else:
    print("F")