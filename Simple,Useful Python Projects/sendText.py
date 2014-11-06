from twilio.rest import TwilioRestClient
#This program sends text messages via twilio, get info, register at https://www.twilio.com
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC13b1a5490f93###################"
auth_token  = "f1594b99b5ae238############"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="#############",    # insert phone number
    from_="1516########.") # insert twilio phone number they give
print message.sid