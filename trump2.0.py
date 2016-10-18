from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
#from string import punctuation
import random


def get_tweet():
    #use the driver and its response the same way you would use requests
    #establish an object instatiation of the webdriver 
    driver = webdriver.Chrome()
    #grab the webpage
    driver_response = driver.get("https://twitter.com/realdonaldtrump?lang=en")
    #make a bs object to parse the html doc
    soup = BeautifulSoup(driver.page_source, "html.parser")
    #makes an object that stores the bs4 parsed html for the tag and class_ specified in the parameters
    #results = soup("p", {"class": "TweetTextSize"})
    results = soup("p", {"class": "js-tweet-text"}, limit = 2)[0]
    #print(results)
    #bad_tag = ['a']
    
    tweet_next = results.find_next('p')
    previous_tweet = tweet_next.find_next('p')
    even_farther = previous_tweet.find_next('p').text.strip()
    print(even_farther)
    #only_tweet = previous_tweet.text.strip()
   
    #print(rand_tweet)
    
    
            

            
        
        
        
    #the tweets var is the soup object that finds all body tags with the class "TweetTextSize" sets the limit to 1 and takes the [0]th element from the list
    #tweets = soup.find_all("p", class_= "TweetTextSize", limit=2)[0]
    #print(type(tweets))
    #tweets = soup.find_all("p", class_= "js-tweet-text")
    #print(tweets)
    #print(type(tweets))
    #print(tweets[0])
    links = soup.find_all("a")
    only_text = results.renderContents()
    #print(only_text)
    #get_tweet = soup.p.get_text()
    find_link = soup.a.get_text()
    #print(find_link)
    
get_tweet()
