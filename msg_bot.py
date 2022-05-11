import pyautogui as pg
import time
import random
import os

os.system('cls')

print("How many different sentences do you want to send?")

choice = int(input("1 - Only ONE / 2 - MORE than ONE: "))

while choice < 1 or choice > 2:
    print("Invalid Choice. Please Try Again:") 
    choice = int(input("1 - Only ONE / 2 - MORE than ONE: "))

if choice == 1:
    msg = str(input("Type your message:\n"))

    actual_qtt = 0

    times_qtt = int(input("How many times do you want to send your message? "))
    while times_qtt <= 0 or times_qtt > 500:
        print("Invalid amount. Please type a number between 1 - 500")
        times_qtt = int(input("How many times do you want to send your message? "))

    time.sleep(5)

    while actual_qtt < times_qtt:
        actual_qtt = actual_qtt + 1
        pg.write(msg)
        pg.press("Enter")
    quit()

elif choice == 2: 
    messages = []
    while True:
        
        msg = str(input("Type your message:\n"))
        messages.append(msg)

        cont_choice = input("Do you want to add one more sentence? (Y/N) ").upper()
        if cont_choice == "Y":
            continue
        else:
            break

    actual_qtt = 0

    times_qtt = int(input("How many times do you want to send your message(s)? "))
    while times_qtt <= 0 or times_qtt > 500:
        print("Invalid amount. Please type a number between 1 - 500")
        times_qtt = int(input("How many times do you want to send your message? "))

    time.sleep(5)

    while actual_qtt < times_qtt:
        pg.write(random.choice(messages))
        pg.press("Enter")
        actual_qtt = actual_qtt + 1
