from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)


def data_refinement(user_query, retreived_data):
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
            "role": "system",
            "content": f"""I am going to ask you a question and my question is {user_query}, which I would like you to answer"
            "based only on the provided context {retreived_data}and the context is , and not any other information."
            "If there is not enough information in the context to answer the question,"
            "Dont say i dont know the answer make"
            "Break your answer up into nicely readable paragraphs".
            "Make the result in maximum 2 lies"
            """,
            }
        ]
    )
    result = completion.choices[0].message.content
    return result