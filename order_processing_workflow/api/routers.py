from fastapi import APIRouter


router = APIRouter(
    tags=["order processing system"],
    responses={404: {"description": "Not found"}},
)

@router.get("/health")
async def health_check():
    return {"status": "API is running"}

@router.post("/verify_order")
async def process_payment():
    return {"message": "Verified order successfully"}

@router.post("/process_payment")
async def process_payment():
    return {"message": "Payment processed successfully"}

@router.post("/update_inventory")
async def update_inventory():
    return {"message": "Inventory updated successfully"}

@router.post("/send_confirmation_email")
async def send_confirmation_email():
    return {"message": "Confirmation email sent successfully"}