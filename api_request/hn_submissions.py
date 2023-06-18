from operator import itemgetter

import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

submissions_ids = r.json()
submission_dicts = []

for submissions_id in submissions_ids[:30]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submissions_id}.json'
    r = requests.get(url)
    print(f'id: {submissions_id}\tstatus: {r.status_code}')
    response_dict = r.json()

    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f'http://news.ycombinator.com/item?id={submissions_id}',
            'comments': response_dict['descendants'],
        }
    except KeyError:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f'http://news.ycombinator.com/item?id={submissions_id}',
            'comments': 0,
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f'\nTitle: {submission_dict["title"]}')
    print(f'\nDiscussion link: {submission_dict["hn_link"]}')
    print(f'\nComments: {submission_dict["comments"]}')