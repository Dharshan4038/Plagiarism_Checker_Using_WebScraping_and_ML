from googleapiclient.discovery import build
def search(keywords):
    api_key = 'AIzaSyBkgLrf-RqqopoUxhqFmkOOrRoy0Bng5SM'
    service = build('customsearch', 'v1', developerKey=api_key)
    result = service.cse().list(q=keywords, cx='9324b599048c04bd5', num=10).execute()
    items = result['items']
    # return items
    # for item in items:
        # print(item['title'])
        # print(item['link'])
        # print(item['snippet'])  
    print(items[0])
    
search("python is a nltk library")