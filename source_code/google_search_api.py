import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

#load api keys from .env file
load_dotenv()

googleapi = os.getenv("GOOGLE_API_KEY")
google_api = googleapi

# this function uses the google api to return a list of linkedin post links based on the search query
def google_search_api(google_search):
    post_links = []
    resource = build("customsearch", 'v1', developerKey=google_api).cse()
    for i in range (1, 100, 10):
        result = resource.list(q=google_search, cx='24ded8702b51b4a21', start=i).execute()
        for items in result['items']:
            post_links.append(items['link'])

    #print(post_links)
    return post_links