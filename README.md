# Linkedin-Post-Scraper

## Description
This Linkedin Post Scraper uses llama 3's Groq API and Google's Custom Search API along with BeautifulSoup to extract posts about a given topic. This program finds the post and determines if it is actually talking about said topic.

The program will extract the following details and write to a CSV file:
1. Author Name (Cleaned)
2. Author LinkedIn Profile Link
3. Post Link

## Installation

In order to run the program, the user must install these Python Libraries and run these commands in their terminal (if not already installed):
```
pip install groq
pip install google-api-python-client
pip install requests
pip install BeautifulSoup4
pip install re
pip install csv
pip install dotenv
```

### API Keys

Before beginning the project you must retrieve two API keys (One for [Groq](https://console.groq.com/docs/quickstart) and one for [Google](https://developers.google.com/custom-search/v1/overview)) by following the links and instructions provided. 

Those keys will be inputed into a .env file to ensure safety and security.

## Source Code Description and Use

### find_keywords.py

This file is in charge of searching taking the input of the user and finding keywords and/or phrases from it. The funciton uses the Llama 3 Groq API to determine the keywords. The role of the API has been altered to only output a list of words. That list of words is returned where it will be sent to create_search.py

### create_search.py

This file takes the list from the previous file and combines them into a valid google search query making sure to only search for posts from LinkedIn. The output of the function will be sent to google_search_api.py.

### google_search_api.py

This file is resonsible for taking the search query returned from the function above and extract the urls of from the search page. Google's Custom Search API is used to create a personal search engine. The number of linked you want to extract is changeable. The links are then put into a list where it is sent to extrack_linkedin_posts.py

### extrack_linkedin_posts.py

This file uses Requests and BeautifulSoup and goes into all the linked from the list above and parses all the required data (author name, thei profile link, and the post contents). Once all the information is extracted, the post will be checked to ensure that it is actually talking about the user's topic. So the post contents are sent to relevance.py to ensure its relevancy. If the post is relavant, the post info will be appended to a list, if not, the program will move to the next post.

### relavance.py

This file uses the Groq API once again to determine its relevancy. The AI has been given a detailed prompt to wire how they should be analyzing the post contents and when the post contents are sent, the API will output a relevancy score out of 100. If the score is greater than 60, then it is deemed to be relevant enough to count as a post.

### WriteToCSV.py

This file is responsible for writing all the post details into a CSV file. This funtion will create a file in the project folder called "posts.csv" and write all the post information into the file.

Once the function has completed writing the to the CSV file, the file will close and the program will shut down.


### Main.py

This file will prompt the user to enter a topic/command and the number of posts they would like to see If they enter an empty string they will be prompted once again to enter a valid input. 

```
Enter the topic you want to find LinkedIn posts on: 
How many posts would you like to see: 
```

Once entered, all the functions defined above will run and completely write to a CSV file.
