import json
import requests
from time import sleep
from google.cloud import pubsub_v1
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "master-reactor-317301-403b51f02b3c.json"
c='San Francisco'
li=[]
def Publish_messages(message):
    publisher = pubsub_v1.PublisherClient()
    project_id="master-reactor-317301"
    topic_id="MyFirstTopic"
    topic_path = publisher.topic_path(project_id, topic_id)
    message_json = json.dumps({'data': {'message': message},})
    message_bytes = message_json.encode('utf-8')
    publisher.publish(topic_path,message_bytes)

for i in range(0,2):
    res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={c}&appid={openweathermap_api_key}&units=imperial')
    li.append(res.json())
    sleep(1)
message=li
Publish_messages(message)