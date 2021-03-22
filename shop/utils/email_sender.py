import requests
import json
from fullecomm.settings import EMAIL_SERVICE_ENDPOINT,EMAIL_SENDER_NAME,EMAIL_SENDER_EMAIL,EMAIL_API_KEY
def sendEmail(name,email,subject,htmlcontent):
    payload = {
        "sender": {
        "name": EMAIL_SENDER_NAME,
        "email": EMAIL_SENDER_EMAIL
        },
        "to": [
            {
            "email": email,
            "name": name
            }
        ],
        "replyTo": {
            "email": EMAIL_SENDER_EMAIL,
            "name": EMAIL_SENDER_NAME
                },
    "htmlContent": htmlcontent,
    "subject": subject
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "api-key": EMAIL_API_KEY
        }

    response = requests.request("POST", EMAIL_SERVICE_ENDPOINT, data=json.dumps(payload), headers=headers)

    return response
#     return requests.post(
# 		"https://api.mailgun.net/v3/sandbox64b041fa08c6435a9dbc57dd9efc8cef.mailgun.org?/messages",
# 		auth=("api", "01cfefc88e08a3d2412781a978fc1593-53c13666-1efd2b66"),
# 		data={"from": "digishop <"+name+"@>sandbox64b041fa08c6435a9dbc57dd9efc8cef.mailgun.org?",
# 			  "to": ['prince14801@gmail.com'],
# 			  "subject": subject,
# 			  "html": htmlcontent})

# print(sendEmail("Amit Yadav","","Testing email","<h1>Hello world</h1>"))
# # print("Amit Yadav")