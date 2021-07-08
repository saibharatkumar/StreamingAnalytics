from time import sleep
from google.cloud import pubsub_v1
from google.auth import jwt

from concurrent import futures
import os
c='San Francisco'
openweathermap_api_key=#apikey
li=[]
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = #private json file
publish_futures = []
from concurrent import futures
def get_callback(publish_future, data):
    def callback(publish_future):
        try:
            pass
            #print(publish_future.result(timeout=60))
        except:
            print(f'Publishing {data} timed out.')
    return callback
def Publish_messages(message):
    publisher = pubsub_v1.PublisherClient()
    project_id=#project_id
    topic_id=#topic_id
    topic_path = publisher.topic_path(project_id, topic_id)
    message_json = json.dumps({'data': {'message': message},})
    message_bytes = message_json.encode('utf-8')
    publish_future = publisher.publish(topic_path,message_bytes)
    publish_future.add_done_callback(get_callback(publish_future, message))
    publish_futures.append(publish_future)
    futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)
for num_messages in range(10):
    li=[]
    for i in range(0,10):
        res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={c}&appid={openweathermap_api_key}&units=imperial')
        li.append(res.json())
        sleep(90)
    message=li
    Publish_messages(message)