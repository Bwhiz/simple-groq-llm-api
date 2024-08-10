import groq
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

#print("successfully imported packages")

groq_client = groq.Groq(api_key=GROQ_API_KEY)

sys_prompt = """
You are a virtual assistant, your goal si to provide useful \
and relevant responses to my query in less than 50 words.
"""

models = [
    "llama-3.1-405b-reasoning",
    "llama-3.1-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]

def generate(model, query, temperature=0):

    response = groq_client.chat.completions.create(
        model = model,
        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": query}
        ],
        temperature = temperature

    )

    answer = response.choices[0].message.content

    return answer

if __name__ == "__main__":
    # sample run:
    query = "what is the capital of Abia state in Nigeria"
    print(generate(models[1], query, temperature=0.1))