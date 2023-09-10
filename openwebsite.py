import webbrowser
import datetime
import time

print("Running openwebsite.py\n")
# Set the URL of the website you want to open
url = input("Enter url:")


print ("Time right now: " + str(datetime.datetime.now().time()))

# Set the time at which you want to open the website
# open_time = datetime.time(11, 1, 00)  # Open at 9:00:00 AM
user_input = input("Enter time to open website (HH MM):")
hour, minute = user_input.split(" ")
open_time = datetime.time(int(hour), int(minute), 00)

print("Website will run @ " + str(open_time) + "\n")


# Wait until the open time
while True:
    now = datetime.datetime.now().time()
    if now >= open_time:
        break
    time.sleep(10)

# Open the website in the default web browser
webbrowser.open(url)


