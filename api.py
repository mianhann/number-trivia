import requests


def get_fact(number):
    url = "http://numbersapi.com/{}".format(number)
    r = requests.get(url)
    if r.status_code == 200:
        return r.text, 0
    
    else:
        print("An error occurred, code={}".format(r.status_code))
        return "", -1