import requests
import json
from fullecomm.settings import EMAIL_SERVICE_ENDPOINT,EMAIL_SENDER_NAME,EMAIL_SENDER_EMAIL,EMAIL_API_KEY
def sendEmail(name,email,subject,htmlcontent):
    payload = {
        "sender": {