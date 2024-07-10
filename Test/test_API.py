import pytest
import allure
from Methods.API import BookSearch

@allure.feature('search books')
class TestBookSearch:

    @allure.story('search book by title')
    def test_search_book_by_title(self):
        title = "дом у озера"
        response = BookSearch.search_by_title(title)
        assert response.status_code == 200
        assert 'products' in response.json()

    @allure.story('search book by author')
    def test_search_book_by_author(self):
        author = "ремарк"
        response = BookSearch.search_by_author(author)
        assert response.status_code == 200
        assert 'products' in response.json()

    @allure.story('search book using filter')
    def test_search_with_filter(self):
        response = BookSearch.search_with_filter()
        assert response.status_code == 200
        assert 'products' in response.json()

    @allure.story('search book with nonexistent title')
    def test_search_nonexistent_title(self):
        non_existent_title = "еотвр23743р"
        response = BookSearch.search_nonexistent_title(non_existent_title)
        assert response.status_code == 200
        assert 'products' in response.json()
        assert len(response.json()['products']) == 0

    @allure.story('search book with special characters in title')
    def test_search_with_special_chars(self):
        special_chars = "!!\\\\\\"
        response = BookSearch.search_with_special_chars(special_chars)
        assert response.status_code == 200
        assert 'products' in response.json()



