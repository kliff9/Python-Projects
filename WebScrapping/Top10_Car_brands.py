import requests
from bs4 import BeautifulSoup
url = requests.get('https://www.mbaskool.com/fun-corner/top-brand-lists/17621-top-10-car-brands-in-the-world.html')

content_html = url.content # The Whole HTML

web = BeautifulSoup(content_html, "html.parser") # An HTML parser takes this string of characters and turns it into a series of events:
#function for displaying Top 10
def top_10(text):
    for slot in text:
        print(slot)

all_h3 = web.find_all('h3') # gather all the h3 elements
ten_to_one = [num.getText() for num in all_h3] # gathers all the text element and appends to the list
one_to_ten = ten_to_one[::-1] # makes the List show backwords
print('Top 10 car brands')
# top_10(one_to_ten)
top_10(ten_to_one)

