import requests
import re
import urllib3
urllib3.disable_warnings()

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
}

def get_content(url):
    response = requests.get(url,headers=headers,verify=False)
    html = response.text
    contents = re.findall('<div class="content">.*?</div>',html,re.S)
    content_lists = []
    for content in contents:
        content = re.sub('<.+?>',"",content)
        content_lists.append(content.strip())
    for content in content_lists:
        print(content)

if __name__ == '__main__':
    base_url = "https://www.qiushibaike.com/text/page/%s/"
    for i in range(1,11):
        new_url = base_url % i
        get_content(new_url)