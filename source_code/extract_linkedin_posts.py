import requests
from bs4 import BeautifulSoup
import re
from relevance import *

# this function uses the url link from create_search_url and extracts the search and post information
def extract_linkedin_posts(linkedin_url, number_of_posts, keyphrases):
    LinkedInPosts = []

    visited_urls = set()

    # Loop through each post on the page
    while len(LinkedInPosts) < number_of_posts:
        
        try:
            for url in linkedin_url:
                
                # checking if the number of relevant posts is equal to the number of posts the user wants
                if len(LinkedInPosts) >= number_of_posts:
                    break

                #checking if the url has already been visited
                if url in visited_urls:
                    continue
                visited_urls.add(url)

                # get the post content using requests and beautifulsoup
                post_content = requests.get(url).text
                soup = BeautifulSoup(post_content, 'html.parser')

                author_element = soup.find('a', class_='text-sm link-styled no-underline leading-open')
                author_uncleaned = author_element.text.strip()
                # cleaning the author name using re library
                author_name_cleaning = re.sub(r'^[^\x00-\x7F]+', '', author_uncleaned).strip()
                author_name = re.sub(r',.*', '', author_name_cleaning).strip()
                #print(author_name)

                author_url = author_element['href']
                #print(author_url)

                post_text = soup.find('p', class_ = 'attributed-text-segment-list__content text-color-text !text-sm whitespace-pre-wrap break-words').text.strip()
                #print(post_text)

                post_info = {
                    'Author': author_name,
                    'Author Profile Link': author_url,
                    'Post Link': url,
                }

                # called the check_relevance function to check if the post is relevant to the topic (post is relevant if the score is greater than 50)
                if check_relevance(post_text, keyphrases):
                    LinkedInPosts.append(post_info)
            
        except:
            print("Error finding posts")
            break

    return LinkedInPosts