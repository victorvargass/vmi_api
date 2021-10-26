from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.vmi import router as VMIRouter
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(VMIRouter, tags=["VMI"], prefix="/vmi")

@app.get("/")
async def index():
    return {"greetings": "Welcome to VMI"}

@app.get("/health")
def health():
    return {"status": "200"}