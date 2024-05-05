from temporalio import workflow
from datetime import timedelta
from activities import process_payment, update_inventory, send_confirmation_email, verify_order

@workflow.defn(sandboxed=False)
class OrderWorkflow:
    @workflow.run
    async def process_order(self, order_id):
        
        result = await workflow.execute_activity(
           verify_order , args=[order_id],
           start_to_close_timeout = timedelta(seconds=5)
        )
        print(result)

        result = await workflow.execute_activity(
            process_payment, args=[order_id],
            start_to_close_timeout = timedelta(seconds=5)
        )
        print(result)

        result = await workflow.execute_activity(
            update_inventory, args=[order_id],
            start_to_close_timeout = timedelta(seconds=5)
        )
        print(result)

        result = await workflow.execute_activity(
            send_confirmation_email, args=[order_id],
            start_to_close_timeout = timedelta(seconds=5)
        )
        print(result)

        return f"Order {order_id} processed successfully"
