# web-scraping-challenge
Step 1 - Scraping:
     import BeautifulSoup,
     import webdriver
     import Browser
     from url=https://mars.nasa.gov/news/ 
     scrape the latest news title and paragragh

JPL Mars Space Images : 
    import splint
    import BeautifulSoup
    from url='https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    scrape the link of full image

Mars Facts
    import pandas
    url='https://space-facts.com/mars/'
    tables=pd.read_html(url)
    df=table[2]
    html_table = df.to_html()

Mars Hemispheres
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemisphere_image_urls  = []
    for item in main_page_items:
    title = item.find('h3').text
    link = 'https://astrogeology.usgs.gov/' + result.find('a', class_='itemLink product-item')["href"]