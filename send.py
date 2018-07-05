#########################
######## Imports ########
#########################

from date_tools import *
from email_tools import *

#########################
### Helper Functions ####
#########################

def gbm_reminder():
    # Get Message
    message = raw_input("Type your message or press enter for default: ")
    if message == "":
        message = "Reminder that we are meeting today at 5:30 PM in GHC 7501!"

    return message, "ScottyLabs GBM Reminder", gbm_datetime()

def hs_reminder():
    # Get Message
    message = raw_input("Type your message or press enter for default: ")
    if message == "":
        message = "Reminder that we have our weekly hack session today at 2:00 PM in WEH 5310!"

    return message, "ScottyLabs Hack Session Reminder", hs_datetime()

def custom_reminder():
    # Get Message
    message = raw_input("Type your message: ")
    subject = raw_input("Type your email subject: ")

    return message, subject, now_datetime()

#########################
### Command Functions ###
#########################

def send_weekly_email():
    # Update Content
    os.system('vim ' + os.path.realpath("content.html"))
    confirm = raw_input("Have you updated the content? (y/n): ")
    if confirm not in [ 'y', 'Y', 'yes' ]:
        print("Quitting...")
        exit()

    # Fetch Skeleton and Content
    skeleton = open("template.html", 'r').read()
    content  = open("content.html", 'r').read()

    # Populate Template
    html = populate(skeleton, content)

    # Get Subject
    subject_code = raw_input("Choose a subject ['+', '-', 'c']: ")
    if subject_code == '+':
        subject = 'ScottyLabs Meetings This Week'
    elif subject_code == '-':
        subject = 'No ScottyLabs Meetings This Week'
    else:
        subject = raw_input("Enter custom subject: ")

    # Send Email
    response = send_message(subject, html)
    print(response.json()['message'])

def send_reminder_email():
    choice = raw_input("Choose the reminder type ['gbm', 'hs', 'c']: ")
    if choice in [ 'g', 'G', 'gbm' ]:
        message, subject, time = gbm_reminder()
    elif choice in [ 'h', 'H', 'hs' ]:
        message, subject, time = hs_reminder()
    else:
        message, subject, time = custom_reminder()

    # Fetch Skeleton and Content
    skeleton = open("reminder.html", 'r').read()

    # Populate Template
    html = populate(skeleton, message)

    # Send Email
    response = send_message(subject, html, time)
    print(response.json()['message'])

#########################
##### Main Function #####
#########################

def main():
    choice = raw_input("Choose the email type ['weekly', 'reminder']: ")
    if choice in [ 'w', 'W', 'weekly' ]:
        send_weekly_email()
    elif choice in [ 'r', 'R', 'reminder' ]:
        send_reminder_email()
    else:
        print("Quitting...")
        exit()

if __name__ == '__main__':
    main()
