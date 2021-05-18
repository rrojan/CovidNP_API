from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pprint


def get_overview_data(soup):
    # get today's and total data elements from soup
    today_data_cards = soup.find("div", class_="todays-data-section").find_all(
        "div",
        class_="ant-card-body",
    )
    total_data_cards = soup.find("div", class_="total-data-section").find_all(
        "div",
        class_="ant-card-body",
    )

    # cleanup data from cards, store in dict and return
    today_fields = ["New Cases", "Recovered", "Deaths"]
    total_fields = ["Total Cases", "Total Infected", "Recovered", "Deaths"]

    today_data_list = [
        int(data.text.replace(str, ""))
        for data, str in zip(today_data_cards, today_fields)
    ]
    total_data_list = [
        int(data.text.replace(str, ""))
        for data, str in zip(total_data_cards, total_fields)
    ]

    today_data = {key: value for key, value in zip(today_fields, today_data_list)}
    total_data = {key: value for key, value in zip(total_fields, total_data_list)}

    return today_data, total_data


def get_data_by_district(soup):
    # get card holding district-wise data
    district_data_card = soup.find(
        "div",
        class_="ant-card",
    )
    print(district_data_card)


def scrape(url):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    driver.get(url)
    # print(driver.page_source)

    soup = BeautifulSoup(driver.page_source, "lxml")

    overview_data = get_overview_data(soup)
    
    try:
        district_card = driver.find_element_by_class_name('data-card')
        print(district_card)
    except:
        print('district wise not found')

    driver.quit()
    return overview_data


if __name__ == "__main__":
    url = "https://covid19.mohp.gov.np/"
    data = scrape(url)
    pprint.pprint(data)
