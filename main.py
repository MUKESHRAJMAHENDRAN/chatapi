from fastapi import FastAPI
from pydantic import BaseModel
from gpt_tool import data_refinement
from utils import data

app = FastAPI()

class UserInput(BaseModel):
    input_text: str

class ResponseOutput(BaseModel):
    output_text: str

@app.post("/chat", response_model=ResponseOutput)
async def chat_api(user_input: UserInput):
    user_text = user_input.input_text
    modified_text = data_refinement(user_text, data)
    return {"output_text": modified_text}
