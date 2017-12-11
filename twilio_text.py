from twilio.rest import Client
import time

auth_token = 'MY_AUTH_TOKEN'
acct_SID = 'MY_ACCT_SID'

print('Sending a text...')
time.sleep(3)

newClient = Client(username=acct_SID, password=auth_token)
new_message = newClient.messages.create(
    to="YOUR_NUMBER",
    from_="MY_NUMBER",
    body="Yo, this is an app texting your phone!"
)

new_message_data = newClient.messages(new_message.sid).fetch()

print('Status = {}, Direction = {}'.format(
    new_message_data.status, new_message_data.direction))
