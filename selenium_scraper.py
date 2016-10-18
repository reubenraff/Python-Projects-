import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import string


def scrape():
    #runs webdriver .exe file
    driver = webdriver.Chrome()
    #shold work like the get from the requests lib 
    driver_response = driver.get('http://www.bevmo.com/catalog/product/view/id/11798')
    #soup obj that takes the driver.page source which is html and parses it with the html default parser
    soup = BeautifulSoup(driver.page_source, "html.parser")
    #price, discount, product title
    results_price = soup("span", {'class':'price'}) # returns a result set (list) #$23.99
    #print(results_price[0])#23.99
    #print(results_price[2].extract())#19.99  #is it [2] because it is the 3rd element in the resultsSet list obj ? 
    for element in results_price[0]:
        if element != string.punctuation:
            print("the regular price of the product is", element)
    for element in results_price[2]:
        if element != string.punctuation:
            print("the discounted price of the product is", element)

scrape()










