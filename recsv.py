import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore



async def on_event(partition_context, event):
    # Print the event data.
    print("Received the event: \"{}\" from the partition with ID: \"{}\"".format(event.body_as_str(encoding='UTF-8'), partition_context.partition_id))

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    print("second wait")
    await partition_context.update_checkpoint(event)

async def main():
    # Create an Azure blob checkpoint store to store the checkpoints.
    checkpoint_store = BlobCheckpointStore.from_connection_string("DefaultEndpointsProtocol=https;AccountName=stos;AccountKey=UbUg2Ahj6hxka/zwEHf96bv9+CwfNt6VVVccdz/+i/Wmr5CkU8zjr1KbmyJYYm/C38r4XrPb4KRgqOo/20el8Q==;EndpointSuffix=core.windows.net", "tst")

    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string("Endpoint=sb://eventhuboq.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=GDos7jZReQqmfPOj/Yj9cQj+x37Budrb80qTaUvA4Sk=", consumer_group="$Default", eventhub_name="eventhubtv", checkpoint_store=checkpoint_store)
    async with client:
        # Call the receive method. Read from the beginning of the partition (starting_position: "-1")
        print("first wait")
        await client.receive(on_event=on_event,  starting_position="-1")


loop = asyncio.get_event_loop()

loop.run_until_complete(main())

