# this function will return a google search url for linkedin posts based on the keyphrases
def create_search_url(keyphrases):
    # Base URL for Google search
    base_url = "site:linkedin.com/posts"
    
    # Format the keyphrases into a single query string
    query = ' OR '.join([f'"{phrase}"' for phrase in keyphrases])
    
    # Construct the full search URL
    search_url = f'{base_url} ({query})'
    #print(search_url)
    
    return search_url