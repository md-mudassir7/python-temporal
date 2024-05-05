import requests
from temporalio import activity


@activity.defn
async def verify_order(order_id):
    try:
        response = requests.post("http://localhost:8000/verify_order", json={"order_id": order_id})
        if response.status_code == 200:
            return "Order verified successfully"
        else:
            raise Exception("Failed to verify order")
    except requests.exceptions.RequestException:
        raise Exception("Failed to reach verification server")

@activity.defn
async def process_payment(order_id):
    try:
        response = requests.post("http://localhost:8000/process_payment", json={"order_id": order_id})
        if response.status_code == 200:
            return "Payment processed successfully"
        else:
            raise Exception("Failed to process payment")
    except requests.exceptions.RequestException:
        raise Exception("Failed to reach payment server")

@activity.defn
async def update_inventory(order_id):
    try:
        response = requests.post("http://localhost:8000/update_inventory", json={"order_id": order_id})
        if response.status_code == 200:
            return "Inventory updated successfully"
        else:
            raise Exception("Failed to update inventory")
    except requests.exceptions.RequestException:
        raise Exception("Failed to reach inventory server")

@activity.defn
async def send_confirmation_email(order_id):
    try:
        response = requests.post("http://localhost:8000/send_confirmation_email", json={"order_id": order_id})
        if response.status_code == 200:
            return "Confirmation email sent successfully"
        else:
            raise Exception("Failed to send confirmation email")
    except requests.exceptions.RequestException:
        raise Exception("Failed to reach email server")
