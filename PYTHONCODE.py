import random 
name = str(input("What is your first name?: "))
name2 = str(input("What is your last name?: "))

print("Hi there, "  +  name + name2 + ", nice to meet you")

nam = int(input("How old are you? "))

if(nam == 17):
    print(str(nam) + "is a good age.")
if(nam <= 17):
    print("You are old enough to drive.")
else:
    print("Your parents need to take you home we don't want you here.")
    
bruh = input("So, " + name + ", how are you today?")
jeff = random.randint(1,5)
if(bruh == "Happy"):
    print(str(input("You are happy. \n That is good to hear. \n Tell me more.")))
else:
    print("That is not good to hear")

if(jeff == 1):
    print("ADAM IS NOT VERY WHITE")
elif(jeff == 2):
    print("YES")
elif(jeff == 3):
    print("I AM YES")
elif(jeff == 4):
    print("WHO IS NOT YES")
elif(jeff == 5):
    print("YES IS YES BUT NOT YES BUT ALSO YES")