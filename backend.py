from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="Enter your api key here")  # Replace with your actual API key

# Initialize FastAPI app
app = FastAPI()

# Enable CORS so frontend can access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify your frontend domain)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request body structure
class GrammarRequest(BaseModel):
    sentence: str

# Define the correction endpoint
@app.post("/correct")
async def correct_text(request: GrammarRequest):
    prompt = f"""
You are a grammar correction assistant. 
Input sentence: "{request.sentence}"

1. Correct the sentence.
2. List the grammar/spelling errors and the corrections.

Respond in the following format:
Corrected: <corrected sentence>
Errors:
- "<wrong part>" → "<correction>"
    """

    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return {"result": response.text}
