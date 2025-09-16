from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Predefined fraud law mapping
fraud_laws = {
    "upi": {
        "law": "Section 66C & 66D of IT Act, 2000 (Identity Theft & Cheating by Personation)",
        "complaint": "I am writing to report unauthorized UPI transactions from my bank account. The fraudster impersonated and cheated me using digital payment platforms."
    },
    "atm": {
        "law": "Section 420 IPC & Section 66 of IT Act (Cheating & Computer-related offenses)",
        "complaint": "I wish to lodge a complaint regarding unauthorized ATM withdrawals. My ATM card details were misused without my consent."
    },
    "identity": {
        "law": "Section 66C IT Act (Identity Theft)",
        "complaint": "My personal identity details were stolen and misused online. I request strict action against the offender."
    },
    "cyberbullying": {
        "law": "Section 67 IT Act (Publishing/Transmitting Obscene Content), Section 354D IPC (Cyberstalking)",
        "complaint": "I am facing repeated harassment and abusive messages online. This constitutes cyberbullying and stalking."
    }
}


@app.get("/")
def root():
    return {"message": "Hello Cyber Sahayak"}


@app.get("/law/{fraud_type}")
def get_law(fraud_type: str):
    fraud_type = fraud_type.lower()
    if fraud_type in fraud_laws:
        return {"fraud_type": fraud_type, "law": fraud_laws[fraud_type]["law"], "complaint": fraud_laws[fraud_type]["complaint"]}
    else:
        return {"error": "Fraud type not found. Try: upi, atm, identity, cyberbullying"}
@app.get("/guidance")
def get_guidance():
    return {"law": "Section 66C: Identity Theft", "steps": ["File FIR", "Keep digital evidence"]}
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class UserQuery(BaseModel):
    query: str

@app.post("/get-guidance")
def get_guidance(user: UserQuery):
    # For now, return dummy guidance
    if "upi" in user.query.lower():
        return {
            "law": "Section 66C – Identity Theft (IT Act)",
            "steps": [
                "Report to bank immediately",
                "File complaint at cybercrime.gov.in",
                "Register FIR with police"
            ]
        }
    else:
        return {
            "law": "Section 66D - Cheating by Impersonation (IT Act)",
            "steps": [
                "Collect all evidence",
                "File complaint at cybercrime.gov.in",
                "Visit nearest cyber cell"
            ]
        }
    # Pydantic model for the incoming data
class Complaint(BaseModel):
    description: str

@app.get("/")
def read_root():
    return {"Hello": "Cyber Sahayak"}

# New endpoint to receive the complaint description
@app.post("/submit_complaint")
def submit_complaint(complaint: Complaint):
    # For now, just print the received description and return a success message.
    # Later, you will add the AI and rule-based logic here.
    print(f"Received complaint: {complaint.description}")
    return {"message": "Complaint received successfully!", "received_description": complaint.description}
class FraudRequest(BaseModel):
    fraud_type: str

@app.get("/")
def root():
    return {"message": "Hello Cyber Sahayak"}

@app.post("/ai-guide")
def ai_guide(request: FraudRequest):
    fraud_type = request.fraud_type

    # Dummy AI logic
    if fraud_type.lower() == "upi fraud":
        law = "Section 66C, IT Act 2000"
        steps = ["Freeze your UPI ID", "File complaint on cybercrime.gov.in", "Contact your bank immediately"]
    else:
        law = "Section 420, IPC"
        steps = ["File FIR at nearest police station", "Collect all digital evidence"]

    return {
        "fraud_type": fraud_type,
        "law": law,
        "steps": steps
    }