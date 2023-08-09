import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


env_path = Path('.')/'.env'

load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
## Sending SIGNING SECREAT , '/slack/events', app(webserver) to web server
slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'],'/slack/events',app) 

client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])

## chat_postmessage is used here to post text messsage in yhe channel that we have created 
client.chat_postMessage(channel='#new-bot',text = 'Hello World') 

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event',{})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    client.chat_postMessage(channel=channel_id,text = text) 




if __name__ == "__main__":
    app.run(debug=True)