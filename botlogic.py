from bs4 import BeautifulSoup
import requests

url = "https://software.cisco.com/download/release.html"

querystring = {"mdfid":"284389362","flowid":"79160","softwareid":"282046477"}
querystring01 = {"mdfid":"286306100","flowid":"79971","softwareid":"282074295"}
querystring02 = {"mdfid":"282774230","flowid":"7445","softwareid":"280805680"}

payload = ""
headers = {
    'authorization': "Bearer MjgzYzk2MjEtYzRlMC00ZjAyLTkwNjUtOGFhZDFjODBiODA2MzNkNDkwNDUtNTZi",
    'cache-control': "no-cache",
    'postman-token': "3c8e20be-3c60-f5e4-6680-209b085a2f97"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
soup = BeautifulSoup(response.text, 'html.parser')
fo = open("foo.txt", "r+")
fo.write(str(soup))
fo.close()

fp = open("foo.txt","r")
for line in fp:
    if "Product:" in line:
        print(fp.next())
    if "mdfTree.addElementRel" in line:
        print(line.split(",")[2])