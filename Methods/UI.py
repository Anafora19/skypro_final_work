from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookStore:
    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self):
        self.driver.get("https://www.chitai-gorod.ru/")

    def search_by_title(self, title):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(title)
        search_box.send_keys(Keys.RETURN)

    def search_by_author(self, author):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(author)
        search_box.send_keys(Keys.RETURN)

    def go_to_section(self, section):
        sections = {
            "Акции": "//a[text()='Акции']",
            "Распродажа": "//a[text()='Распродажа']",
            "Каталог": "//a[text()='Каталог']",
            "Что ещё почитать": "//a[text()='Что ещё почитать']"
        }
        self.driver.find_element(By.XPATH, sections[section]).click()

    def check_books_present(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-card__title")))

        