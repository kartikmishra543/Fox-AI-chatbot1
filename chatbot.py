from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def get_response(question):
    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=question
    )
    return response.output_text