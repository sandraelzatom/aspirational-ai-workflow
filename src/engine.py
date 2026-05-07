import openai
from pydantic import BaseModel

class LegalResponse(BaseModel):
    analysis: str
    citations: list
    confidence_score: float

def generate_implementation(context, query):
    # System prompt loaded from /prompts/
    system_prompt = open("../prompts/system_v1.txt").read()
    
    response = openai.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context: {context}\nQuery: {query}"}
        ],
        response_format=LegalResponse,
    )
    return response.choices[0].message.parsed
