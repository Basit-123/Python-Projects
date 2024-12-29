#1- twilio client setup
#2- input user
#3- Scheduling logics
#4 -message Send

#step 1 install required liabraries
from twilio.rest import Client
from datetime import datetime,timedelta
import time


#step-2 twilio credencial
account_sid = 'AC696a7d3eb0ccb1717662967d4b863b6e'
auth_token = 'cbf16eee35569d0061c2d1e368ff25d5'

client = Client(account_sid, auth_token)

#step-3 design send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
        from_='whatsapp:14155238886',
        body=message_body,
        to=f"whatsapp:{recipient_number}"
        )

        print(f'Message send successfully! Message SID{message.sid}')

    except Exception as e:
        print('An error occurred')    

#step-4 user input

name = input('Enter the recipient name = ')
recipient_number = input('Enter the recipient Whatsapp number with country code (e.g +12345):')
message_body = input(f"Enter the message you want to send to {name}: ")


#step 5 parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24hours format): ')


#datetime 
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate dely
time_difference = schedule_datetime - current_datetime
delay_second = time_difference.total_seconds()

if delay_second <= 0:
    print('The Specified time is in the past. Please enter a future date and time: ')
else:
    print(f'Message Scheduled to be send to {name} at {schedule_datetime}.')

    #wait untill the scheduled time
    time.sleep(delay_second) #1000

    #send the message 
    send_whatsapp_message(recipient_number, message_body)

