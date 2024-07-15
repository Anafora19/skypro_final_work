import pytest
import allure
from selenium import webdriver
from Methods.UI import Bookstore as bookstore_module
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()  # вызов драйвера Firefox.
    yield driver
    driver.quit()

@pytest.fixture(scope="module") 
def bookstore_instance(driver):
    return bookstore_module(driver)  # Использование правильного имени класса

@pytest.mark.usefixtures("bookstore_instance")
class TestBookstore:

    @allure.feature("search book by title")
    def test_search_by_title(self, bookstore_instance):
        bookstore_instance.open_home_page()
        bookstore_instance.search_by_title("гарри поттер")
        assert bookstore_instance.check_books_present(), "books not found by title 'гарри поттер'"

    @allure.feature("search book by author")
    def test_search_by_author(self, bookstore_instance):
        bookstore_instance.open_home_page()
        bookstore_instance.search_by_author("джоан роулинг")
        assert bookstore_instance.check_books_present(), "books not found by author 'джоан роулинг'"

    @allure.feature("search by section акции")
    def test_search_by_promotion_section(self, bookstore_instance):
        bookstore_instance.open_home_page()
        bookstore_instance.click_and_verify("Акции", "/promotions")
        
        # Проверка, что URL изменился на ожидаемый
        assert "/promotions" in bookstore_instance.driver.current_url, "URL did not change to /promotions"
        
    @allure.feature("search by section распродажа")
    def test_search_by_sale_section(self, bookstore_instance):
        bookstore_instance.open_home_page()
        bookstore_instance.click_and_verify("Распродажа", "/sales")
        
        # Проверка, что URL изменился на ожидаемый
        assert "/sales" in bookstore_instance.driver.current_url, "URL did not change to /sales"
        

    @allure.feature("search by section что ещё почитать")
    def test_search_by_recommendation_section(self, bookstore_instance):
        bookstore_instance.open_home_page()
        bookstore_instance.click_and_verify("Что ещё почитать?", "/collections")
        
        # Проверка, что URL изменился на ожидаемый
        assert "/collections" in bookstore_instance.driver.current_url, "URL did not change to /collections"
        