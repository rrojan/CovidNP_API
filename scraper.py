from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


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

    daily_data = {key: value for key, value in zip(today_fields, today_data_list)}
    total_data = {key: value for key, value in zip(total_fields, total_data_list)}

    return daily_data, total_data


def get_data_by_district(driver):
    cards = driver.find_elements_by_class_name("ant-card-grid")

    # clean up card data and store it in a dict
    district_data = []

    for card in cards:
        data = card.text.split("\n")
        district_data.append(
            {
                "District": data[0].replace(" ", "_"),
                "Total": int(data[1].replace("Total: ", "")),
                "Male": int(data[2].replace("Male: ", "")),
                "Female": int(data[3].replace("Female: ", "")),
            }
        )

    return district_data


def scrape(url):
    print("Starting webdriver...")
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    print("Requesting data from url...")
    driver.get(url)
    # pause for a while to let the async calculator thing load
    print("Pausing for 30 seconds to allow everything to load...")
    time.sleep(30)

    print("Parsing data...")
    soup = BeautifulSoup(driver.page_source, "lxml")
    daily_data, total_data = get_overview_data(soup)
    district_wise_data = get_data_by_district(driver)
    return daily_data, total_data, district_wise_data


if __name__ == "__main__":
    url = "https://covid19.mohp.gov.np/"
    scrape(url)
