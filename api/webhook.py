# api/webhook.py

from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/topup")
async def handle_topup_webhook(request: Request):
    data = await request.json()
    print("✅ Webhook masuk:", data)
    return {"status": "success"}
