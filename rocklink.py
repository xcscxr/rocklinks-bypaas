from bs4 import BeautifulSoup 
import requests
import time


def bypass(url):
	code = url.split("/")[-1]
	final_url = "https://link.techyone.co/" + code + "?quelle="

	client = requests.Session()
	resp = client.get(final_url).text
	
	soup = BeautifulSoup(resp, "html.parser")
	params_value = soup.find(id="go-link").find_all(name="input")
	data = {}
	for payload in params_value:
		data[payload.get("name")] = payload.get("value") 
		
		
	headers = {
	           "referer":final_url,
		   "origin":"https://link.techyone.co",
		   "x-requested-with": "XMLHttpRequest",
		   "user-agent":"Mozilla/5.0 (Linux; Android 11; SM-T515) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.13 Safari/537.36"
	}
	
	time.sleep(10)
	r = client.post("https://link.techyone.co/links/go",data=data, headers=headers)
	print(r.text)
	
	
bypass("https://rocklinks.net/XgQox")	






