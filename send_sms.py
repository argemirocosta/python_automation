from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC91ae2a00ee01ab3330aaabc35bffb433"
# Your Auth Token from twilio.com/console
auth_token = "d943a3529cfc8df1d84d2858c75926c8"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5582999200156",
    from_="+19402408397",
    body=f'Testando envio de mensagem de texto')
print(message.sid)
