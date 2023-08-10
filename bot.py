import os
import json
import requests

def lambda_handler(event, context):
    # Extract user's message from the event
    user_message = event.get('text', '').lower()
    
    # Check if the user's message contains "hi"
    if 'hi' in user_message:
        response = "Hi, welcome to the chat bot!"
    else:
        response = "Hello, how can I assist you?"
    
    # Construct the response payload
    response_payload = {
        "text": response
    }
    
    # Get the Slack webhook URL from the environment variable
    webhook_url = os.environ['SLACK_WEBHOOK_URL']
    
    # Send the response payload to Slack using the webhook URL
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, data=json.dumps(response_payload), headers=headers)
    
    # Check the response status and return a success message
    if response.status_code == 200:
        return {
            'statusCode': 200,
            'body': json.dumps('Message sent successfully to Slack')
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': json.dumps('Failed to send message to Slack')
        }
