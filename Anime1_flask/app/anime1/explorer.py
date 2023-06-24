import requests as req
from bs4 import BeautifulSoup
import re

__home_url = "https://anime1.me/"
__data_url = "https://d1zquzjgwo9yb.cloudfront.net/?_=1687014810044"

__header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def get_menu() -> dict:
    reponse = req.get(url = __data_url, headers = __header)
    content = reponse.json()
    
    return {
        "length": len(content),
        "content": content
    }
    
def get_anime_list():
    reponse = req.get(url = __home_url, headers = __header)
    menu_name = re.findall(r'<a href=".+">([0-9]+年[春夏秋冬]季新番)</a>', reponse.text)[0]
    
    sub_reponse = req.get(url = "{}/{}".format(__home_url, menu_name), headers = __header)
    sub_menu_name = re.findall(r"[0-9]+年[春夏秋冬]季\([1-9]+-[1-9]+月\)新番", sub_reponse.text)[0]
    
    sub_content = BeautifulSoup(sub_reponse.text, "html.parser")
    prev_block = sub_content.find("div", class_ = "entry-content")
    prev = prev_block.find("p")
        
    return {
        "main_menu": menu_name,
        "sub_menu": sub_menu_name,
    }   
    
if __name__ == "__main__":
    get_anime_list()