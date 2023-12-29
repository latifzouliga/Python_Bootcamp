# from twilio.rest import Client
#
# # Twilio account credentials
# account_sid = 'YOUR_ACCOUNT_SID'
# auth_token = 'YOUR_AUTH_TOKEN'
# twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'  # Your Twilio phone number (sandbox or purchased)
#
# # Destination WhatsApp number
# whatsapp_to_number = 'whatsapp:+1234567890'  # The recipient's WhatsApp number (including country code)
#
# # Your message
# message_body = 'Hello, this is a WhatsApp message sent using Twilio!'
#
# # Create Twilio client
# client = Client(account_sid, auth_token)
#
# # Send the message
# message = client.messages.create(
#     body=message_body,
#     from_=f'{twilio_phone_number}',
#     to=f'{whatsapp_to_number}'
# )
#
# print(f"Message sent successfully with message SID: {message.sid}")


