import os
from groq import Groq
from dotenv import load_dotenv

# load api keys from .env file
load_dotenv()

# this function uses the Groq API to check if the post content extracted from extract_linkedin_posts() is relevant to the topic
def check_relevance(post_content, topic):

    apikey = os.getenv("GROQ_API_KEY")

    detailed_prompt = f"""
    You are a semantic analyzer. I need you to determine if the following post content is relevant to the topic "{topic}".
    Please consider the context and meaning of the entire post. Only return an output of an score out of 100.

    Post content:
    {post_content}
    """

    client = Groq(
    api_key=apikey,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a semantic analyzer that analyzes and determings whether the given post is relavant to the topic given by the user.\nOutput should only be a relevancy score out of 100 and no other text."
            },
            {
                "role": "user",
                "content": f"{detailed_prompt}.",
            }
        ],
        model="llama3-8b-8192",
        max_tokens=200
    )
    analysis_result = chat_completion.choices[0].message.content
    #print(analysis_result)

    # Extract the score from the analysis result
    if analysis_result:
        score = int(analysis_result)
        return score > 66  # Check if score is greater than 66

    return False