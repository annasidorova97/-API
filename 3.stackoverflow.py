from pprint import pprint
import requests
import datetime


def get_stackoverflow_questions(tags: str, days: int):
    url = 'https://api.stackexchange.com/2.3/questions?'
    unix_data = str(datetime.datetime.now().timestamp())[:-7]
    unix_last_data = str((datetime.datetime.now() - datetime.timedelta(days=days)).timestamp())[:-7]
    params = {'order': 'desc', 'sort': 'creation', 'site': 'stackoverflow', 'tagged': tags,
              'fromdate': unix_last_data, 'todate': unix_data}
    response = requests.get(url, params=params)
    pprint(response.json())


if __name__ == '__main__':
    get_stackoverflow_questions('python', 2)