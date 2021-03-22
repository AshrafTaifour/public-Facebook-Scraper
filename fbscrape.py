from bs4 import BeautifulSoup as soup  # web client, used to obtain webpages

# calls the request module from urllib package. from the request module we import urlopen
from urllib.request import urlopen as uReq


def findHobbies(url: str, visibility: str):
    # will obtain the webpage and download it, this starts a connection
    # NOTE: is it possible to do this as you're logged in? Can you get a page that has extra information (FRIEND HTML PAGE)
    Client = uReq(url)
    page_html = Client.read()  # will store the HTML page into the variable

    Client.close()  # closes connection
    page_soup = soup(page_html, "html.parser")  # will parse the HTML file

    # grabs the 'Favorites' section in facebook for the page
    if visibility is 'visible':
        containers = page_soup.findAll("div", {"class": "mediaPageName"})
    else:
        containers = page_soup.findAll("div", {"class": "uiCollapsedList"})

    print(containers)  # displays parsed data


my_url = 'https://www.facebook.com/YOURPUBLICFACEBOOKURL'

# findHobbies(my_url,'visibile')
findHobbies(my_url, 'invisible')
