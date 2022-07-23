import time
from bs4 import BeautifulSoup
from selenium import webdriver

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
    SCROLL_PAUSE_TIME = 4
    blog_data = []
    for i in range(0, 10):
        # Scroll down to bottom
        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
        # Calculate new scroll height and compare with last scroll height
        print("page scrolling: ", last_height)
        # print(page.text)
        parse = BeautifulSoup(driver.page_source, "html.parser")
        all_blogs = parse.find_all('div', {'class': 'playground-item-col'})
        print(len(all_blogs))
        for blog in all_blogs:
            print("*" * 100)
            # print(blog)
            blog_scrap = dict(
                title=blog.find("h4", class_="playground-title").text,
                description=blog.find("div", class_="playground-excerpt").text,
                blog_image_url=blog.find("div", class_="playground-image").img.get("src"),
                author_name=blog.find("div", class_="playground-author-name").text,
                author_image_url=blog.find("div", class_="playground-author-image").img.get("src"),
                author_designation=blog.find("div", class_="playground-author-description").text,
                reading_time=blog.find("span", class_="playground-read-time-text").text

            )
            print(blog_scrap)
            print("*" * 100)
            if blog not in blog_data:
                blog_data.append(blog_scrap)

    return blog_data


if __name__ == '__main__':
    blogs = scrap_blog_data()
