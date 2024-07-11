import pytest
import allure
from selenium import webdriver
from Methods.UI import BookStore

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  #Вызов драйвера Chrome.
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def bookstore(driver):
    return bookstore(driver)  

@pytest.mark.usefixtures("bookstore")
class TestBookstore:

    @allure.feature("search book by title")
    def test_search_by_title(self, bookstore):
        bookstore.open_home_page()
        bookstore.search_by_title("гарри поттер")
        assert bookstore.check_books_present(), "Books not found by title 'гарри поттер'"

    @allure.feature("search book by author")
    def test_search_by_author(self, bookstore):
        bookstore.open_home_page()
        bookstore.search_by_author("джоан роулинг")
        assert bookstore.check_books_present(), "Books not found by author 'джоан роулинг'"

    @allure.feature("search by section акции")
    def test_search_by_promotion_section(self, bookstore):
        bookstore.open_home_page()
        bookstore.go_to_section("акции")
        assert bookstore.check_books_present(), "Books not found in section 'акции'"

    @allure.feature("search by section распродажа")
    def test_search_by_sale_section(self, bookstore):
        bookstore.open_home_page()
        bookstore.go_to_section("распродажа")
        assert bookstore.check_books_present(), "Books not found in section 'распродажа'"

    @allure.feature("search by section каталог")
    def test_search_by_catalog_section(self, bookstore):
        bookstore.open_home_page()
        bookstore.go_to_section("каталог")
        assert bookstore.check_books_present(), "Books not found in section 'каталог'"

    @allure.feature("search by section что ещё почитать")
    def test_search_by_recommendation_section(self, bookstore):
        bookstore.open_home_page()
        bookstore.go_to_section("что ещё почитать")
        assert bookstore.check_books_present(), "Books not found in section 'что ещё почитать'"

        