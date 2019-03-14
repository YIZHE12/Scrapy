# Scrapy_tutorials
### Tutorials using scrapy in Python for web scrapping
source:
https://docs.scrapy.org/en/latest/intro/tutorial.html
https://www.youtube.com/watch?v=ak0rRAtTqf0&index=4&list=PLE50-dh6JzC6dHxpAno-a6W7QpWdAFN20
https://www.youtube.com/watch?v=BhBVLErss24&list=PLZs3Tlv3d6Gmyf42z2lCn99keDLoh0lpq&index=83

To use scrappy:
1. Create project in command line:
scrapy startproject project_name

2. Give a name to the crawler in the python script:
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    ....
    
3. Use the spider in command line:
scrapy crawl quotes -o example.csv -t csv

Alternatively, can call shell in command line
scrapy shell 'https://....'

Exit shell using Ctrl + V/D

4. Note you have to define items in the item.py first before calling

5. Install Google Chrome Xpath Help to text xpath command



