from fastapi import FastAPI

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
