from instamojo_wrapper import Instamojo
from fullecomm.settings import PAYMENT_API_AUTH_TOKEN,PAYMENT_API_KEY 

api = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')


# Create a new Payment Request
response = api.payment_request_create(
    amount='20',
    purpose='Testing ke liye',
    send_email=True,
    email="yadavamit14801@gmail.com",
    redirect_url="http://www.google.com"
    )
# print the long URL of the payment request.
url=response['payment_request']['longurl']
# print the unique ID(or payment request ID)
print(url)