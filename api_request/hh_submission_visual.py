from operator import itemgetter
import requests
from plotly import offline

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

submissions_ids = r.json()
submission_dicts = []
for submissions_id in submissions_ids[:50]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submissions_id}.json'
    r = requests.get(url)
    response_dict = r.json()

    try:
        submission_dict = {
            'author': response_dict['by'],
            'title': response_dict['title'],
            'hn_link': f'http://news.ycombinator.com/item?id={submissions_id}',
            'comments': response_dict['descendants'],
        }
    except KeyError:
        submission_dict = {
            'author': response_dict['by'],
            'title': response_dict['title'],
            'hn_link': f'http://news.ycombinator.com/item?id={submissions_id}',
            'comments': 0,
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles, hn_links, comments = [], [], []
for submission_dict in submission_dicts:
    author = submission_dict['author']
    title = submission_dict['title']
    link = submission_dict['hn_link']
    hn_link = f"<a href='{link}'>{author}</a>"
    comment = submission_dict['comments']

    titles.append(title)
    hn_links.append(hn_link)
    comments.append(comment)

data = [{
    'type': 'bar',
        'x': hn_links,
        'y': comments,
        'hovertext': titles,
        'marker': {
            'color': 'rgb(60,100,150)',
            'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
        },
        'opacity': 0.6
}]

my_layout = {
    'title': 'Most popular discussions on Hacker-News',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Author',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='article_hn.html')