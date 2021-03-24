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
    df=table[0]
    df = df.rename(columns={0: "Description", 1: "Mars"})
    df = df.set_index("Description")
    html_table = df.to_html()

Mars Hemispheres
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemisphere_image_urls  = []
    for item in main_page_items:
    title = item.find('h3').text
    link = 'https://astrogeology.usgs.gov/' + result.find('a', class_='itemLink product-item')["href"]


Step 2 MongoDB and Flask Application

    1) converting Jupyter notebook into a Python script, name scrape_mars.py.
    2)create a route " /scrape", import scrape_mars.py to the route.
    3) Create a root route " /", query Mongo database and pass the mars data into an HTML template.
    4) Create a template HTML file "index.html", display all of the data in HTML.
    5) apply bootstrap to "index.html.
    6) choose "mark down", insert image in Jupyter notebook to finish screen shot of final html.