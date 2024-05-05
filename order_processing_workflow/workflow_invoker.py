import asyncio
import sys
from temporalio import client

async def invoke_order_workflow(order_id):
    temporal_client = await client.Client.connect("localhost:7233")

    workflow_handle = await temporal_client.start_workflow(
        "OrderWorkflow",
        order_id,
        id=f"OrderWorkflow-{order_id}",  
        task_queue="OrderProcessingTaskQueue",
    )

    result = await workflow_handle.result()
    print(f"Workflow completed with result: {result}")


if __name__== "__main__":
    asyncio.run(invoke_order_workflow(sys.argv[1]))
