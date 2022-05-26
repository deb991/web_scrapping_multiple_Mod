'''Web scrapping using BS4 -- Mod 1'''
import mechanicalsoup
from bs4 import BeautifulSoup
from urllib.request import urlopen
from mechanicalsoup.browser import Browser

'''Creating Beautifulsoap object'''
url = 'http://olympus.realpython.org/profiles/dionysus'
#url = 'http://olympus.realpython.org/profiles'
page = urlopen(url)
html_data = page.read().decode('utf-8')
soup = BeautifulSoup(html_data, 'html.parser')

#print('soup testing:\t', soup.text)
print('soup Image Find:\t', soup.find("img"))


def link_list_test():
    base_url = 'http://olympus.realpython.org/'
    test_page = urlopen(base_url + '/profiles')
    test_data = test_page.read().decode('utf-8')

    '''Creating Beautifulsoap object'''

    test_soap = BeautifulSoup(test_data, "html.parser")

    '''Now trying to access all the links are available 
    & associated with this link'''

    for link in test_soap.find_all("a"):
        link_url = base_url + link['href']
        print('Link:\t', link_url)


if __name__ == '__main__':
    link_list_test()