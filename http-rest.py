import requests
import time
import schedule
import sys

def Response():
    url = 'https://www.google.com'
    r = requests.post(url)
    try:
        print('the response time is' , r.elapsed.total_seconds())
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

Response()





#sys.stdout = open('sample.txt', 'a')
#schedule.every(5).seconds.do(Response)
#sys.stdout.close()




#while True:
#    schedule.run_pending()
#    time.sleep(1)
#    f = open('sample.txt', 'a')
#    f.write(str(Response))
#    f.close



