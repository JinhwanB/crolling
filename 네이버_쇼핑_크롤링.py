from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 네이버 쇼핑 중 식품 카테고리에서 가장 많이 팔린 상품 크롤링
dr = webdriver.Chrome()
dr.get("https://www.naver.com") # 네이버 홈페이지 진입

dr.find_element(By.CSS_SELECTOR, "#NM_FAVORITE > div.group_nav > ul.list_nav.type_fix > li:nth-child(5) > a").click() # 쇼핑 메뉴 클릭
time.sleep(2)

dr.find_element(By.CSS_SELECTOR, "#__next > div > div.pcHeader_header__tXOY4 > div > div > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._siteButton_site_button_mUZWX > a._siteButton_link_best_3Y9cW._siteButton_link_3vUut.N\=a\:SNB\.best100").click() # 쇼핑 best 메뉴 클릭
time.sleep(2)

dr.find_element(By.CSS_SELECTOR, "#container > div:nth-child(2) > div.home_title_area__G5x__ > div > a").click()
time.sleep(2)

dr.find_element(By.CSS_SELECTOR, "#container > div:nth-child(2) > div.home_title_area__G5x__ > div > ul > li:nth-child(1) > a").click()
time.sleep(2)

dr.find_element(By.CSS_SELECTOR, "#container > div:nth-child(2) > div.home_list_area__dAYBN > div.categoryFilter_filter_wrap__fkQxn > ul > li:nth-child(8) > a").click() # 식품 카테고리 클릭
time.sleep(2)

dr.find_element(By.CSS_SELECTOR, "#container > div:nth-child(2) > div.home_btn_area__fecZO > a").click() #더보기 클릭
time.sleep(2)

dr.find_element(By.CSS_SELECTOR, "#container > div > div > div.category_category_contents__oVtaX > div.rankFilter_tab_area__zqI0L.rankFilter_type_four__DiSzx > a:nth-child(2)").click() # 많이 구매한 상품 클릭
time.sleep(2)

# 화면 끝까지 스크롤
current_scroll = dr.execute_script("return document.body.scrollHeight")

while True:
    dr.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    scroll_height = dr.execute_script("return document.body.scrollHeight")
    if current_scroll == scroll_height:
        break
    else:
        current_scroll = dr.execute_script("return document.body.scrollHeight")
time.sleep(2)
# 화면 끝까지 스크롤 끝

# 내용 크롤링
results = []
count = 1

for i in range(1, 91):
    url1 = "/html/body/div/div/div[3]/div/div/div[2]/div[3]/div[1]/ul/li[{}]/div[2]/div[2]".format(i)
    url2 = "/html/body/div/div/div[3]/div/div/div[2]/div[3]/div[1]/ul/li[{}]/div[2]/div[1]/strong".format(i)
    product_title = dr.find_element(By.XPATH, url1).text
    product_price = dr.find_element(By.XPATH, url2).text
    product_link = dr.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div[2]/div[3]/div[1]/ul/li[{}]/a".format(i))
    link = product_link.get_attribute("href")
    result = {count: product_title, "price": f"{product_price}원", "link": link}
    results.append(result)
    count += 1

print(results)
print(len(results))
# 크롤링 끝

