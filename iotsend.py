import uuid
import datetime
import random
import json
import asyncio

from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData




async def run():
    while True:
        await asyncio.sleep(5)
        # Create a producer client to produce and publish events to the event hub.
        producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://eventhuboq.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=GDos7jZReQqmfPOj/Yj9cQj+x37Budrb80qTaUvA4Sk=", eventhub_name="eventhubtv")   # For each device, produce 20 events.
        async with producer:
            event_data_batch = await producer.create_batch() # Create a batch. You will add events to the batch later.
            reading = {'id': str(uuid.uuid4()), 'tv':random.choice(['LG','Samsung','SOLAR','OK','Philips','Hitachi']), 'timestamp': str(datetime.datetime.utcnow()), 'temperature': random.randint(70, 100), 'powerConsumption': random.randint(40, 150)}
            s = json.dumps(reading) # Convert the reading into a JSON string.
            event_data_batch.add(EventData(s)) # Add event data to the batch.
            await producer.send_batch(event_data_batch) # Send the batch of events to the event hub.
            print(s)
            print("iot Sent!!")


loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(run())
    loop.run_forever()
finally:
    print("Closing Loop")
    loop.close()