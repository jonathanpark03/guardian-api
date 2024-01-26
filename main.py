import requests
import json

baseurl = "https://content.guardianapis.com/"

key = "api-key=fe29790f-0168-4d4f-bc10-ebe3f25bce14"

content = "search?"

q = "q=economics%20OR%20finance&"

date = "from-date=2023-11-22&"

pageSize = "page-size=50&"

r = requests.get(baseurl + content + q + date + pageSize + key)

data = r.json()

# pages = data["response"]["pages"] # include this to retrieve every article
pages = 2 # will retrieve 2 pages of 50 articles
currPage = 1

with open("./guardian.json", "w") as output: # clears json file
    output.truncate()

with open("./guardian.json", "a") as output:
    while currPage <= pages:
        pageEndpoint = "page=" + str(currPage) + "&"
        r = requests.get(baseurl + content + pageEndpoint + q + date + pageSize + key)
        data = r.json()
        json.dump(data, output)
        currPage += 1
