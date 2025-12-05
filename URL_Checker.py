'''
Docstring for Semester Project.URL_Checker

To-Do:

File reader
status code meaning
use status code to indicate broken links?
maybe use get and if it throws an error tell user its not a correct link?
'''


import requests

class URL:

    def __init__(self,urls):

        self.urls = urls

        self.status = requests.get(urls).status_code

    
    def getStatusCode(self):
        #Make into switch statment return not just number but reason like OK, changing protocols, etc.
        return self.status
    


Done = False

list_o_URL = []


while not Done:

    url=input("Please enter your urls, If you are finished type 'done' ")

    if(url == 'done'):

        Done = True
    
    else:

        list_o_URL.append(URL(url))

for url in list_o_URL:

    print(f"URL: {url.urls} Status code: {url.getStatusCode()}")
