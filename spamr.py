import pyautogui
import time

msg = input("Enter the message to be spammed")
n = input("How many times to spam?")

print("Sending in")

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Initiating send")

for i in range(0,int(n)):
	pyautogui.typewrite(msg + '\n')
