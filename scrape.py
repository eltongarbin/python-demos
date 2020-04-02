import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        vote = subtext[idx].select('.score')
        if len(vote) == 0:
            continue

        points = int(vote[0].getText().replace(' points', ''))
        if points < 100:
            continue

        hn.append({
            'title': item.getText(),
            'link': item.get('href', None),
            'votes': points
        })

    return hn


def get_stories(num_pages):
    data = list()

    for i in range(num_pages):
        res = requests.get(
            f'https://news.ycombinator.com/news?p={i + 1}')
        soup = BeautifulSoup(res.text, 'html.parser')

        links = soup.select('.storylink')
        subtext = soup.select('.subtext')

        data.extend(create_custom_hn(links, subtext))

    return data


pprint.pprint(sort_stories_by_votes(get_stories(2)))
