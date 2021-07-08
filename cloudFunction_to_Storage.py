import base64
import pandas as pd
from google.cloud import storage
import os
import json
import operator as op
import numpy as np
import time


def upload_data_to_bucket(df,file_name):
    storage_client = storage.Client()
    bucket_name = #bucket_name
    bucket=storage_client.get_bucket(bucket_name)
    new_blob=bucket.blob(f'{file_name}'+str(time.time())+'.csv')
    new_blob.upload_from_string(data=df.to_csv(index=False))

    
def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = #private_json_key
    # print(pubsub_message)
    df=pd.DataFrame(json.loads(pubsub_message)['data']['message'])
    # print()
    # print(df)
    df['lon']=df['coord'].map(op.itemgetter('lon'))
    df['lat']=df['coord'].map(op.itemgetter('lat'))
    df['Temperature'] = df['main'].map(op.itemgetter('temp'))
    df['Humidity'] = df['main'].map(op.itemgetter('humidity'))
    df['Wind Speed'] = df['wind'].map(op.itemgetter('speed'))
    df=df[['name','lon', 'lat','Temperature','Humidity','Wind Speed']]
    upload_data_to_bucket(df,"firstfile")