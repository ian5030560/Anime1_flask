import requests as req
from bs4 import BeautifulSoup

__url = "https://d1zquzjgwo9yb.cloudfront.net/?_=1687014810044"

__header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def explore() -> dict:
    reponse = req.get(url = __url, headers = __header)
    content = reponse.json()
    
    return {
        "length": len(content),
        "content": content
    }
    