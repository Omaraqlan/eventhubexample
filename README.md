# eventhubexample
this example is to simulate iot data in event hub and recieving from event hub with checkpoint.
files:

iotsend.py --- to simulate IOT sensors
send.py --- to simulate batch data
recsv.py --- to read data from eventhubs
if you dont need checkpoint please use this file https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/eventhub/azure-eventhub/samples/sync_samples/recv.py  and inside function onevent() put event.body_as_str(encoding='UTF-8')
