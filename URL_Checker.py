'''
Name: Carlos Lucero
Date:12/08/25
Description:
This program takes either a file or user input of urls. Then using requests and status codes outputs to console
if a link is broken or not.
'''

import os
import requests

class URL:

    def __init__(self,url):

        response = requests.get(url, timeout=10, allow_redirects=True)
        #Holds url that was entered
        self.urls = url
        #Holds status code
        self.status = response.status_code
        #If redirect occurs then new url will be here
        self.finalUrl = response.url

    
    def getStatus(self):
        #Checks if url request was successful
        if(self.status == 200):

            return "(200 O.K) Link is working"
        
        else:
            #Match case for diffrent http status codes
            match self.status:

                case 301:
                
                    return (f"(301 Moved Permanently) Redirected to: {self.final_url}")
                
                case 302:
                    
                    return (f"(302 Found) Temporarily redirected to: {self.final_url}")
            
                case 307:
                    
                    return (f"(307 Temporary Redirect) to: {self.final_url}")
                case 308:
                    
                    return (f"(308 Permanent Redirect) to: {self.final_url}")

                case 404:

                    return ("(404 Not Found) Link is broken")
                
                case 400:

                    return ("(400 Bad Request) Link is broken or User Error")
                
                case 403:

                    return ("(403 Forbidden) Link is broken")
                
                case 401:

                    return ("(401 Unauthorized) Link is broken")
                
                case 503:

                    return ("(503 Service Unavailable) Link is temporarly broken, try again later")
                
                case 500:

                    return ("(500 Internal Server Error) Link is temporarly broken due to server issue, try again later")
                
                case _:
                    
                    return (f"Link status: {self.status}")

selector = input("For reading urls from a file enter 1,For enter urls manualy press 2:\n")

validInput = False

list_o_URL = []
#This will loop until user inputs 1 or 2 for the selector
while not validInput:

    if(selector == '1'):

        validInput = True

        fileFound = False
        #keeps program from continuing until given a file that exists
        while not fileFound:

            file = input("Please enter the file the contains the URLS\n")
            
            if os.path.exists(file):

                #Reads urls from provided file
                with open(file, 'r') as f:

                    for line in f:

                        list_o_URL.append(URL(line.strip()))
                
                fileFound = True

            else:

                print(f"{file} does not exist")
    
    elif(selector == '2'):

        validInput = True

        Done = False

        #Loops until user enters done
        while not Done:

            url=input("Please enter your urls, If you are finished type 'done' ")

            if(url == 'done'):

                Done = True
    
            else:

                list_o_URL.append(URL(url))


    else:

        Selector = input("Invalid Selection: For reading urls from a file enter 1,For enter urls manualy press 2:\n")
#prints out urls and their statuses 
for url in list_o_URL:

    print(f"URL: {url.urls} Status code: {url.getStatus()}")

