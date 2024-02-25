def radius_to_degrees(radius_km):
    earth_circumference_km = 40075.0  # Earth's circumference at the equator

    degrees = (2 * radius_km / earth_circumference_km) * 360
    return degrees

# Example usage
radius = 1.57  # Replace with your actual radius in kilometers
degrees = radius_to_degrees(radius)
print(f"{radius} kilometers is approximately {degrees} degrees.")


# send sms messages
from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse

#simona twilio number
account_sid = 'AC2bd599b7a96b862203a1033787206ad0'
auth_token = '9bee2c8690898fa80c70c05a857e7bbd'
from_number = '+12055396017'

#  Data structure to store users and their locations
users = [
    {'phone_number': '+917028886778', 'latitude': 19.4370, 'longitude': 72.7851},
    {'phone_number': '+919867043783', 'latitude': 19.4370, 'longitude': 72.7851},
    {'phone_number':' +917028082779', 'latitude':  19.4370, 'longitude': 72.7851}

]

# # Function to check if a location triggers an alert
def check_alert_condition(user_latitude, user_longitude, target_latitude, target_longitude, radius):
    distance = ((user_latitude - target_latitude)**2 + (user_longitude - target_longitude)**2)**0.5
    return distance < radius

def send_alerts(users, target_latitude, target_longitude, alert_radius):
    client = Client(account_sid, auth_token)

    for user in users:
        to_number = user['phone_number']
        user_latitude = user['latitude']
        user_longitude = user['longitude']
        if check_alert_condition(user_latitude, user_longitude, target_latitude, target_longitude, alert_radius):
            message = client.messages.create(
                body='🚨 Emergency Alert 🚨\nMissile Threat Detected. Take Immediate Shelter!\n - Move to a basement or an interior room.\n - Avoid windows and stay low.\n - If outside, seek the nearest sturdy shelter.\nStay tuned for updates from authorities. This is NOT a drill.\nFollow local emergency instructions.\nStay Safe! : https://www.example.com',
                from_=from_number,
                to=to_number
            )
            print(f"SMS alert sent to {to_number}. SID: {message.sid}")
            twiml_response = VoiceResponse()
            twiml_response.gather(action='/handle-key', numDigits=1)
            twiml_response.say("""<speak xml:space="preserve">
          This is an emergency alert. 
          Please visit our website for more information: 
          <a href="https://www.example.com">https://www.example.com</a>.
       </speak>""")

            # Make the voice call
            call = client.calls.create(
                to=to_number,
                from_=from_number,
                twiml=str(twiml_response)
            )

            print(f"Voice alert call initiated to {to_number}. SID: {call.sid}")
        else:
            print(f"No alert triggered for {to_number}")


# # # Function to send an SMS alert to users whose locations match the condition
# def send_sms_alerts(target_latitude, target_longitude, alert_radius, alert_message):
#     client = Client(account_sid, auth_token)
#
#     for user in users:
#         user_latitude = user['latitude']
#         user_longitude = user['longitude']
#
#         if check_alert_condition(user_latitude, user_longitude, target_latitude, target_longitude, alert_radius):
#             to_number = user['phone_number']
#             message = client.messages.create(
#                 body=alert_message,
#                 from_=from_number,
#                 to=to_number
#             )
#             print(f"SMS alert sent to {to_number}. SID: {message.sid}")
#         else:
#             print(f"No alert triggered for {user['phone_number']}")
#
#
#
# # voice alerts
#
# # Function to send voice alerts to multiple recipients
# def send_voice_alerts(users, target_latitude, target_longitude, alert_radius, alert_message):
#     client = Client(account_sid, auth_token)
#
#     for user in users:
#         to_number = user['phone_number']
#         user_latitude = user['latitude']
#         user_longitude = user['longitude']
#
#         if check_alert_condition(user_latitude, user_longitude, target_latitude, target_longitude, alert_radius):
#             twiml_response = VoiceResponse()
#             twiml_response.gather(action='/handle-key', numDigits=1)
#             twiml_response.say(alert_message)
#
#             # Make the voice call
#             call = client.calls.create(
#                 to=to_number,
#                 from_=from_number,
#                 twiml=str(twiml_response)
#             )
#
#             print(f"Voice alert call initiated to {to_number}. SID: {call.sid}")
#         else:
#             print(f"No alert triggered for {to_number}")


# data from nukemap
target_latitude = 19.4370
target_longitude = 72.7851
alert_radius = degrees
# alert_message = '🚨 Emergency Alert 🚨\nMissile Threat Detected. Take Immediate Shelter!\n - Move to a basement or an interior room.\n - Avoid windows and stay low.\n - If outside, seek the nearest sturdy shelter.\nStay tuned for updates from authorities. This is NOT a drill.\nFollow local emergency instructions.\nStay Safe!'


send_alerts(users, target_latitude, target_longitude, alert_radius)
# send_sms_alerts(target_latitude, target_longitude, alert_radius, alert_message)
# send_voice_alerts(users, target_latitude, target_longitude, alert_radius, alert_message)
# J8BKNJRQCPXW882MWUK65HEP