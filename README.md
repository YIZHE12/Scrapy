# Scrapy_
### Scrapy in Python for web scrapping
source:
https://docs.scrapy.org/en/latest/intro/tutorial.html
https://www.youtube.com/watch?v=ak0rRAtTqf0&index=4&list=PLE50-dh6JzC6dHxpAno-a6W7QpWdAFN20
https://www.youtube.com/watch?v=BhBVLErss24&list=PLZs3Tlv3d6Gmyf42z2lCn99keDLoh0lpq&index=83

#### Install:
```
pip3 install scrapy

pip3 install pypiwin32 (on windows)
```

#### Tips to use scrappy:
1. Create project in command line:
scrapy startproject project_name

2. Generate a python file in the spider folder

    Give a name to the crawler in the python script:
    class QuotesSpider(scrapy.Spider):
        name = "spider_name"
        ....

    or use 'scrapy genspider spider_name xxx.com' in command line to alternative generate the python file

3. Use the spider in command line:
    scrapy crawl quotes -o example.csv -t csv

    You can also call shell in command line
    scrapy shell 'https://....'
    
    Also create a python file to run command line, here, I created a start.py which use 
    
    cmdline.execute("scarpy crawl qsbk_spider".split()) to run 

Exit shell using Ctrl + V/D

4. Note you have to define items in the item.py first before calling

5. Install Xpath Helper in Google Chrome to text xpath command or Xpath Checker at Firefox

5. Go to settings.py change
```
    ROBOTSTXT_OBEY = True to False
    remove comments in:
    DEFAULT_REQUEST_HEADERS = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Language': 'en',
      'User-Agent':xxx 
    }
```    
    information of User-Agent can be found in Ispect mode - Network - Google.com - User-Agent




