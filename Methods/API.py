import requests

class BookSearch:
    base_url = "https://www.chitai-gorod.ru/"  # Убедитесь, что этот URL правильный

    @classmethod
    def search_by_title(cls, title):
        try:
            response = requests.get(f"{cls.base_url}/search", params={"phrase": title})
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")

    @classmethod
    def search_by_author(cls, author):
        try:
            response = requests.get(f"{cls.base_url}/search", params={"phrase": author})
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")

    @classmethod
    def search_with_filter(cls, filter_value):
        try:
            url = f"{cls.base_url}/catalog/books/"
            params = {"filter": filter_value}
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
        return None

    @classmethod
    def search_nonexistent_title(cls, title):
        try:
            response = cls.search_by_title(title)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")

    @classmethod
    def search_with_special_chars(cls, chars):
        try:
            response = requests.get(f"{cls.base_url}/search/product", params={"phrase": chars})
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")