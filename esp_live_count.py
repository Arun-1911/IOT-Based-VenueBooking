import requests

def get_live_count():
    try:
        response = requests.get("http://172.20.10.2/")
        if response.status_code == 200:
            html = response.text
            return int(html.split("People Count: ")[1].split("</h1>")[0])
    except:
        return "Unavailable"
