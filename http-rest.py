import requests

def Response():
    url = 'https://www.google.com'
    r = requests.post(url)
    try:
        print('the response time is' , r.elapsed.total_seconds())
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

Response()





