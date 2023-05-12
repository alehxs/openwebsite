import webbrowser
import datetime
import time

print("Running openwebsite.py\n")
# Set the URL of the website you want to open
url = ''


print ("Time right now: " + str(datetime.datetime.now().time()))
# Set the time at which you want to open the website
open_time = datetime.time(13, 45, 00)  # Open at 9:00:00 AM
print("Website will run @ " + str(open_time) + "\n")


# Wait until the open time
while True:
    now = datetime.datetime.now().time()
    if now >= open_time:
        break
    time.sleep(1)

# Open the website in the default web browser
webbrowser.open(url)


