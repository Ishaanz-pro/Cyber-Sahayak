from fastapi import FastAPI
app = FastAPI(title="Cyber Sahayak")

@app.get("/")
def root():
    return {"message": "Hello Cyber Sahayak"}
