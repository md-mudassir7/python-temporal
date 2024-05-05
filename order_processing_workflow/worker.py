import asyncio
from temporalio import worker, client
from workflow import OrderWorkflow
from activities import process_payment, update_inventory, send_confirmation_email, verify_order

async def main():
    temporal_client = await client.Client.connect("localhost:7233")

    async with worker.Worker(
        temporal_client,
        task_queue="OrderProcessingTaskQueue",
        workflows=[OrderWorkflow],
        activities=[verify_order, process_payment, update_inventory, send_confirmation_email],
    ):
        print("Worker started. Waiting for tasks...")
        await asyncio.Future()

asyncio.run(main())
