import requests
import time
crash = input("It seems something went wrong :c would you like to send a detailed description of what happened to the dev?\n")
if crash.lower == 'yes' or 'y':
    webhook = 'INSERT WEBHOOK HERE'
    msg = input("Write a description of what happened:\n")
    try:
        data = requests.post(webhook, json={'content': msg})
        if data.status_code == 204:
            print(f"Sent bug report: {msg}")
            exit()
    except:
        pass