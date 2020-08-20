import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&radius=25&l=%EC%84%9C%EC%9A%B8&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

print(indeed_result.text)

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

print(pagination)