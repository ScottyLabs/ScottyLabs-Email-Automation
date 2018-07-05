#########################
######## Imports ########
#########################

from date_tools import *
import settings

import webbrowser
import os
import requests

#########################
###### Mailgun API ######
#########################

def send_message(subject, html, date=now_datetime()):
    return requests.post(
        "https://api.mailgun.net/v3/" + settings.domain + "/messages",
        auth=("api", settings.api_key),
        data={"from": settings.sender,
              "to": settings.recepients,
              "subject": subject,
              "html": html,
              "o:deliverytime": date})

#########################
# Email HTML Generator ##
#########################

def populate(skeleton, body):
    # Merge Content with Template
    html = skeleton.replace('[[[_markdown]]]', body)

    # Write Merged Email into tmp.html
    populated = open("tmp.html", 'w+')
    populated.write(html)
    populated.close()

    # Visual Check
    webbrowser.open_new_tab("file://" + os.path.realpath("tmp.html"))
    confirm = raw_input("Does the output look okay? (y/n): ")
    if confirm not in [ 'y', 'Y', 'yes' ]:
        print("Quitting...")
        exit()

    # Remove tmp.html
    os.remove("tmp.html")

    return html
