import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

from scrap_app.models import Blog

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


BASE_URL = 'https://proshore.eu/resources/'


def scrap_blog_data():
    url = BASE_URL
    print("url: ", url)
    driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)
    driver.get(url)
    time.sleep(8)
    last_height = driver.execute_script("return document.body.scrollHeight")
    SCROLL_PAUSE_TIME = 50
    blog_data = []
    time.sleep(SCROLL_PAUSE_TIME)
    for i in range(0, 2):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
        time.sleep(5)
        # Calculate new scroll height and compare with last scroll height
        print("page scrolling: ", last_height)
        # print(page.text)
        parse = BeautifulSoup(driver.page_source, "html.parser")
        all_blogs = parse.find_all('div', {'class': 'playground-item-col'})
        print(len(all_blogs))
        for blog in all_blogs:
            print("*" * 100)
            # print(blog)
            print("title: ", blog.find("h4", class_="playground-title").text, "Loop: ", i)

            title = blog.find("h4", class_="playground-title")
            description = blog.find("div", class_="playground-excerpt")
            blog_image_url = blog.find("div", class_="playground-image")
            author_name = blog.find("div", class_="playground-author-name")
            author_image_url = blog.find("div", class_="playground-author-image")
            author_designation = blog.find("div", class_="playground-author-description")
            reading_time = blog.find("span", class_="playground-read-time-text")

            blog_scrap = dict(
                title=title.text,
                description=description.text,
                blog_image_url=blog_image_url.img.get("src"),
                author_name=author_name.text if author_name is not None else None,
                author_image_url=author_image_url.img.get("src") if author_image_url is not None else None,
                author_designation=author_designation.text if author_designation is not None else None,
                reading_time=reading_time.text if reading_time is not None else None

            )
            print("*" * 100)
            if blog not in blog_data:
                df = pd.DataFrame([blog_scrap])
                df.to_csv("blogs_data.csv", mode='a', index=False, header=False)
                blog_data.append(blog_scrap)

    return blog_data


if __name__ == '__main__':
    blogs = scrap_blog_data()
