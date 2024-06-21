'''
Plan:
1. user prompted for topic 
2. use groq api to break down their input to a list of ten similar key phrases
3. use those key phrases to search linkedin posts using google search api
4. extract the linkedin posts and info using beautiful soup or selenium
5. use groq api to look at the posts and see if they are actually talking about the topic
6. if so, save results to csv file
'''

from find_keywords import *
from create_search import *
from google_search_api import *
from extract_linkedin_posts import *
from write_to_csv import *

if __name__ == "__main__":
    # Get the topic from the user
    topic = input("Enter the topic you want to find LinkedIn posts on: ")
    while True:
        number_of_posts = int(input("How many posts would you like to see: "))
        if 1 <= number_of_posts:
            keyphrases = find_keywords_groq(topic)
            google_search = create_search_url(keyphrases)
            linkedin_url = google_search_api(google_search)
            post_info = extract_linkedin_posts(linkedin_url, number_of_posts, keyphrases)
            write_to_csv(post_info)
            break
        else:
            print("Please enter a positive number.")
            continue