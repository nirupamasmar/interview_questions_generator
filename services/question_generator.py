import requests
from config import GROQ_API_KEY, GROQ_BASE_URL, LLAMA_MODEL

def qa_generator_agent(job_role: str) -> str:
    messages = [{
        "role":"system",
        "content":(
            "You are expert interview questions genrator agent."
            "On the basis of job description provided you have to genrate 15-20 questions which are helpful for user."
            "Your task is to only generate questions, don't give answers or explanation."
        )},
        {
            "role":"user",
            "content":job_role
        }

    ]

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model":LLAMA_MODEL,
        "messages":messages,
        "temperature":0.7
    }

    response = requests.post(GROQ_BASE_URL,headers=headers, json=payload)
    response.raise_for_status()
    result= response.json()
    return result["choices"][0]["message"]["content"]