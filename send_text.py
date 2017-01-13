from twilio.rest import TwilioRestClient

account_sid = "AC5f9c7b646cd3e1fe4da7c49286cbd7cb" # Your Account SID from www.twilio.com/console
auth_token  = "5ea800dce2c7ad796daf641f4ca9b071"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is Alexandre",
    to="+5511963589989",    # Replace with your phone number
    from_="+16782164065") # Replace with your Twilio number

print(message.sid)
