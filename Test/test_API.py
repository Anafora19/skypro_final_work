import pytest
import allure
from Methods.API import BookSearch
from bs4 import BeautifulSoup

@allure.feature('search books')
class TestBookSearch:

    @allure.story('search book by title')
    def test_search_book_by_title(self):
        title = "дом у озера"
        response = BookSearch.search_by_title(title)
        assert response is not None, "No response from server"
        assert response.status_code == 200
        html = response.text
        print(f"Response HTML for title '{title}': {html[:500]}")  # Логирование первых 500 символов HTML
        soup = BeautifulSoup(html, 'html.parser')
        products = soup.find_all('div', class_='product-title__head')
        assert products, f"No products found for the given title: {title}"
        print(f"Found {len(products)} products for title: {title}")

    @allure.story('Search book by author')
    def test_search_book_by_author(self):
        author = "ремарк"
        response = BookSearch.search_by_author(author)
        assert response is not None, "No response from server"
        assert response.status_code == 200
        html = response.text
        print(f"Response HTML for author '{author}': {html[:500]}")  # Логирование первых 500 символов HTML
        soup = BeautifulSoup(html, 'html.parser')
        products = soup.find_all('div', class_='product-title__author')
        assert products, f"No products found for the given author: {author}"
        print(f"Found {len(products)} products for author: {author}")

    @allure.story('Search book using filter')
    def test_search_with_filter(self):
        filter_value = "fantastika-fehntezi"
        response = BookSearch.search_with_filter(filter_value)
        assert response is not None, "No response from server"
        assert response.status_code == 200
        html = response.text
        print(f"Response HTML with filter: {html[:500]}")  # Логирование первых 500 символов HTML
        soup = BeautifulSoup(html, 'html.parser')
        products = soup.find_all('div', class_='product-card__text')
        assert products, "No products found with the given filter"
        print(f"Found {len(products)} products with the filter")

    @allure.story('search book with nonexistent title')
    def test_search_nonexistent_title(self):
        non_existent_title = "еотвр23743р"
        response = BookSearch.search_by_title(non_existent_title)
        assert response is not None, "no response from server"
        assert response.status_code == 200
        html = response.text
        print(f"Response HTML for nonexistent title '{non_existent_title}': {html[:500]}")  # Логирование первых 500 символов HTML
        soup = BeautifulSoup(html, 'html.parser')
        products = soup.find_all('div', class_='product-card__text')
        assert len(products) == 0, "Expected no products for nonexistent title but found some"

    @allure.story('search book with special characters in title')
    def test_search_with_special_chars(self):
        special_chars = "!!\\\\\\"
        response = BookSearch.search_with_special_chars(special_chars)
        assert response is not None, "no response from server"
        assert response.status_code == 200
        html = response.text
        print(f"Response HTML for special characters '{special_chars}': {html[:500]}")  # Логирование первых 500 символов HTML
        soup = BeautifulSoup(html, 'html.parser')
        products = soup.find_all('div', class_='product-card__text')
        assert len(products) == 0, "Expected no products for special characters but found some"