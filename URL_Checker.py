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

    
    def getStatus(self):
        #Make into switch statment return not just number but reason like OK, changing protocols, etc.
        if(self.status == 200):

            return "(200 O.K) Link is working"
        
        else:

            match self.status:

                case 404:

                    return ("(404 Not Found) Link is broken")
                
                case 400:

                    return ("(400 Bad Request) Link is broken or User Error")
                
                case 403:

                    return ("(403 Forbidden) Link is broken")
                
                case 401:

                    return ("(401 Unauthorized) Link is broken")
                
                case _:
                    return "Link is broken"
    
Selector = input("For reading urls from a file enter 1,For enter urls manualy press 2:\n")

validInput = False

while not validInput:

    if(Selector == '1'):

        validInput = True
       
        print("File handling goes here")
    
    elif(Selector == '2'):

        validInput = True

        Done = False

        list_o_URL = []


        while not Done:

            url=input("Please enter your urls, If you are finished type 'done' ")

            if(url == 'done'):

                Done = True
    
            else:

                list_o_URL.append(URL(url))

            
        for url in list_o_URL:

            print(f"URL: {url.urls} Status code: {url.getStatus()}")

    else:

        Selector = input("Invalid Selection: For reading urls from a file enter 1,For enter urls manualy press 2:\n")



