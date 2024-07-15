import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import unittest

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Bookstore:
    def __init__(self, driver):
        self.driver = driver

    def close_popup(self):
        try:
            popup = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".change-city__button--accept"))
            )
            popup.click()
            logger.info("Всплывающее окно закрыто")
        except Exception as e:
            logger.info("Всплывающее окно не найдено или уже закрыто")

    def open_home_page(self):
        logger.info("Открытие главной страницы")
        self.driver.get("https://www.chitai-gorod.ru/")
        self.close_popup()
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.header-search__input"))
            )
            logger.info("Главная страница загружена")
        except Exception as e:
            logger.error(f"Ошибка при загрузке главной страницы: {e}")
            self.driver.save_screenshot("open_home_page_error.png")
            raise

    def search_by_title(self, title):
        logger.info(f"Поиск книги по названию: {title}")
        self.close_popup()
        try:
            search_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.header-search__input"))
            )
            search_box.clear()
            search_box.send_keys(title)
            search_box.send_keys(Keys.RETURN)
            logger.info("Поиск выполнен")
        except Exception as e:
            logger.error(f"Ошибка при поиске книги по названию: {e}")
            self.driver.save_screenshot("search_by_title_error.png")
            raise

    def search_by_author(self, author):
        logger.info(f"Поиск книги по автору: {author}")
        self.close_popup()
        try:
            search_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.header-search__input"))
            )
            search_box.clear()
            search_box.send_keys(author)
            search_box.send_keys(Keys.RETURN)
            logger.info("Поиск выполнен")
        except Exception as e:
            logger.error(f"Ошибка при поиске книги по автору: {e}")
            self.driver.save_screenshot("search_by_author_error.png")
            raise

    def check_books_present(self):
        logger.info("Проверка наличия книг")
        self.close_popup()
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-card__title"))
            )
            logger.info("Книги найдены")
            return True
        except Exception as e:
            logger.error(f"Ошибка при проверке наличия книг: {e}")
            self.driver.save_screenshot("check_books_present_error.png")
            raise

    def click_and_verify(self, link_text, expected_url_part):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, link_text))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(
            EC.staleness_of(element)
        )
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(expected_url_part)
        )
        assert expected_url_part in self.driver.current_url, f"Expected URL part '{expected_url_part}' not found in '{self.driver.current_url}'"

    def test_navigation_links(self):
        self.click_and_verify("Акции", "/promotions")
        self.driver.get("https://www.chitai-gorod.ru/")  # Возвращаемся на главную страницу
        self.click_and_verify("Распродажа", "/sales")
        self.driver.get("https://www.chitai-gorod.ru/")  # Возвращаемся на главную страницу
        self.click_and_verify("Что ещё почитать?", "/collections")

class NavigationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        cls.driver.get("https://www.chitai-gorod.ru/")
        cls.bookstore = Bookstore(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_navigation_links(self):
        self.bookstore.test_navigation_links()

        
if __name__ == "__main__":
    unittest.main()