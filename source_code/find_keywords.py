import os
from groq import Groq
from dotenv import load_dotenv

# loading in api keys from the .env file
load_dotenv()

def find_keywords_groq(topic):
    apikey = os.getenv("GROQ_API_KEY")
    # Break down the topic into keywords/phrases
    client = Groq(
        #api_key=os.environ.get("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"),
        api_key=apikey,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a helpful key word generator.\nAll outputs is only written in a numbered list format with no intro sentence."
            },
            {
                "role": "user",
                "content": f"{topic}. Give me a list of ten similar key words or phrases to the most inportant phrase in the topic.",
            }
        ],
        model="llama3-8b-8192",
        max_tokens=75
    )

    keyword_api_out = (chat_completion.choices[0].message.content)
    lines = (keyword_api_out.strip().split("\n"))
    
    keyphrases = [line.split('. ', 1)[1] for line in lines if '. ' in line]
    #print(keyphrases)
    return keyphrases