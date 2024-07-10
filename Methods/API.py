import requests

class BookSearch:
    base_url = "https://www.chitai-gorod.ru"

    @classmethod
    def search_by_title(cls, title):
        response = requests.get(f"{cls.base_url}/search/product", params={"phrase": title})
        response.raise_for_status()
        return response

    @classmethod
    def search_by_author(cls, author):
        response = requests.get(f"{cls.base_url}/search/product", params={"phrase": author})
        response.raise_for_status()
        return response

    @classmethod
    def search_with_filter(cls):
        response = requests.get(f"{cls.base_url}/products", params={"include": "producttexts,publisher,publisherbrand,publisherseries,dates,literatureworkcycle,rating"})
        response.raise_for_status()
        return response

    @classmethod
    def search_nonexistent_title(cls, title):
        response = requests.get(f"{cls.base_url}/search/product", params={"phrase": title})
        response.raise_for_status()
        return response

    @classmethod
    def search_with_special_chars(cls, chars):
        response = requests.get(f"{cls.base_url}/search/product", params={"phrase": chars})
        response.raise_for_status()
        return response
    
    