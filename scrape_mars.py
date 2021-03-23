from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def create_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    return browser

# Visit mars.nasa.gov/news
def scrape_title_and_paragraph():
    browser = create_browser()
    listings={}
    url='https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(3)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the latest tile and paragraph
    results = soup.find('li', class_='slide')

    news_title = results.find('div', class_='content_title').text
    news_p = results.find('div', class_='article_teaser_body').text

    browser.quit()
    return news_title, news_p



def scrape_marsimage():
    url='https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser = create_browser()
    browser.visit(url)
    time.sleep(2)

    html=browser.html
    soup = bs(html, 'html.parser')
    image=soup.find('img',class_='headerimage fade-in')

    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/' + image['src']
    
    browser.quit()
    return featured_image_url


def scrape_marsfact():
    import pandas as pd
    url='https://space-facts.com/mars/'

    tables=pd.read_html(url)
    df=tables[0]
    df = df.rename(columns={0: "Description", 1: "Mars"})
    df = df.set_index("Description")
    html_table = df.to_html()
    return html_table


def scrape_marsHemispheres():
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser = create_browser()
    browser.visit(url)
    time.sleep(2)

    html=browser.html
    soup = bs(html, 'html.parser')

    main_page_items = soup.find_all('div',class_='item')

    hemisphere_image_urls  = []
    for item in main_page_items:
        title = item.find('h3').text
        link = 'https://astrogeology.usgs.gov/' + item.find('a', class_='itemLink product-item')["href"]
    
        browser.visit(link)
        time.sleep(2)
        linked_page = bs(browser.html, 'html.parser')
        full_link = linked_page.find('div', class_='downloads').find('a')["href"]
    
        hemisphere_image_urls.append({"title": title, "img_url": full_link})

    browser.quit()
    return hemisphere_image_urls

def scrape():
    dictionary = {}
    dictionary["news_title"], dictionary["news_paragraph"]  = scrape_title_and_paragraph()
    dictionary["mars_image"] = scrape_marsimage()
    dictionary["Mars_fact"]=scrape_marsfact()
    dictionary["hemisphere_list"]=scrape_marsHemispheres()
    return dictionary
