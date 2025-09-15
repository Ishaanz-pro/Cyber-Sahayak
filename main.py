from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Cyber Sahayak"}

@app.get("/guidance/{category}")
def get_guidance(category: str):
    guidance_map = {
        "upi_fraud": [
            "Step 1: Immediately call your bank and request UPI hotlisting.",
            "Step 2: Change your UPI PIN.",
            "Step 3: Report the fraud at the NCRP portal (cybercrime.gov.in).",
            "Step 4: Keep all transaction IDs handy."
        ],
        "social_media": [
            "Step 1: Take screenshots of abusive content.",
            "Step 2: Use in-app reporting (Instagram, Facebook, etc.).",
            "Step 3: File complaint at NCRP portal.",
            "Step 4: Contact local cyber police if threat persists."
        ]
    }
    return {"category": category, "steps": guidance_map.get(category, ["No guidance available for this category."])}
