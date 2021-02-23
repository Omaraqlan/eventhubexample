import time
import os
import uuid
import datetime
import random
import json

from azure.eventhub import EventHubProducerClient, EventData

# This script simulates the production of events for 10 devices.
tvBrandList=['LG','Samsung','SOLAR','OK','Philips','Hitachi']
devices = []
for x in range(0, 10):
    devices.append(str(uuid.uuid4()) +'-'+ random.choice(tvBrandList))

# Create a producer client to produce and publish events to the event hub.
producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://eventhuboq.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=GDos7jZReQqmfPOj/Yj9cQj+x37Budrb80qTaUvA4Sk=", eventhub_name="eventhubtv")

for y in range(0,20):    # For each device, produce 20 events.
    event_data_batch = producer.create_batch() # Create a batch. You will add events to the batch later.
    for dev in devices:
        # Create a dummy reading.
        reading = {'id': dev, 'tv':dev.split('-')[-1], 'timestamp': str(datetime.datetime.utcnow()), 'temperature': random.randint(70, 100), 'powerConsumption': random.randint(40, 150)}
        s = json.dumps(reading) # Convert the reading into a JSON string.
        event_data_batch.add(EventData(s)) # Add event data to the batch.
    producer.send_batch(event_data_batch) # Send the batch of events to the event hub.

# Close the producer.
producer.close()