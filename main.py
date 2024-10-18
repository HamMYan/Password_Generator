import string
import random


def generate_password(theLength):
    letters = string.ascii_letters
    digits = string.digits
    totalChars = letters + digits
    finalResult = ""

    for i in range(theLength):
        finalResult += random.choice(totalChars)

    return finalResult


def main():
    while True:
        print("Enter the password length")
        thelength = input()

        try:
            thelength = int(thelength)
        except:
            print("Wrong password length")
            continue

        thePassword = generate_password(thelength)
        print("The Password is :", thePassword)
        break


main()
