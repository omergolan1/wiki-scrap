"""
author:  omer golan
date:    1/12/19 grade(10)
destniy: connect between 2 wiki pages in the shortest way

using: beautiful soup 4, requests
python version: 3.7
"""

import time
import requests
import bs4
import sys
sys.setrecursionlimit(200)
Found=True
counter=0




#enter 2 wiki subjects
first_subject=input("enter first subject: ") #first url
second_subject=input("enter second subject: ") #the url that you want to find

print('https://en.wikipedia.org/wiki/'+first_subject) #print the first url

res=requests.get('https://en.wikipedia.org/wiki/'+first_subject) # get the first wiki page

soup = bs4.BeautifulSoup(res.text,"html.parser") #parse to html
res.close()
for link in soup.find_all('a', title=True):

    if link['title'].lower()==second_subject.lower(): # chek if the url title equal to the second subject

        print("https://en.wikipedia.org/"+link['href']) #print the second subject link
        print(second_subject + " found ")
        Found=False
        break


if Found:  #chek if the second url was'nt found in the first page

    for link1 in (soup.find_all('a', title=True)):        #loop all the links in the first page
        link_url="https://en.wikipedia.org/"+link1['href'] #link url = new link in fisrt page
        res=requests.get(link_url)                          # get the new link
        soup = bs4.BeautifulSoup(res.text, "html.parser")   #parse to html
        counter+=1
        if counter<=150 and Found != False:        # search limit and also check if not found answer
            for link in soup.find_all('a', title=True):    # search the second subject inside the new link page 2

                if link['title'].lower() == second_subject.lower(): # search the second subject
                    print(link_url) #print the previos link

                    print("https://en.wikipedia.org/" + link['href'])  #print the answer link
                    print(second_subject + " found\n ")
                    counter+=1
                    Found = False
                    res.close()
                    break
        else:           #if not found in 2 link exemple>> cat>night vison>human eye
            break







res.close()




