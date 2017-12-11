from twilio.rest import Client
import time

auth_token = '034050e5dfdd7a77ad5adeb91f3dcc77'
acct_SID = 'AC68700b29508ba3e1f3e7c06c6ae52e02'

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
