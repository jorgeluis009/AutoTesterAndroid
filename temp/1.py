from twilio.rest import Client

account_sid = 'AC712f31fe10da3cc6a40dd716d01502f3'
auth_token = 'd1e1f8005238203a18a84c3ee4ea6a81'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+524492595229',
                        from_='+17547048255'
                        )
print(call.sid)
