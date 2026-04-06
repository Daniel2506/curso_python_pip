import requests

def get_categories():
    response = requests.get('https://api.escuelajs.co/api/v1/categories')
    if response.status_code == 200:
        return response.json()
    else:
        return []
