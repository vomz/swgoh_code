from __future__ import print_function

import time
from collections import namedtuple

import requests
from bs4 import BeautifulSoup as Soup
from pprint import pprint


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te - ts))
        return result

    return timed


class Collections:
    Toon = namedtuple('Toon', 'name link star level gear')

    @timeit
    def __init__(self, user):
        self.session = requests.session()
        self.user = user
        r = self.session.get('https://swgoh.gg/u/{}/collection'.format(user))
        self.collection = Soup(r.text, 'html.parser')
        # collect the characters that are unlocked
        self.toons = []
        self._populate_toons()

    def _populate_toons(self):
        raw = self.collection.find_all('div', 'col-xs-6 col-sm-3 col-md-3 col-lg-2')
        for cur_toon in raw:
            name = cur_toon.find("div", {"class": "collection-char-name"}).text
            link = cur_toon.find('a', 'collection-char-name-link')['href']
            try:
                level = int(cur_toon.find("div", {"class": "char-portrait-full-level"}).text)
                inactive = len(cur_toon.find_all("div", {"class": 'star-inactive'}))
                star = len(cur_toon.find_all("div", {"class": 'star'})) - inactive
                gear = cur_toon.find("div", {"class": "char-portrait-full-gear-level"}).text
            except AttributeError:
                # character not owned
                level = 0
                star = 0
                gear = 0
            self.toons.append(Collections.Toon(name, link, star, level, gear))

    @property
    def num_toons(self):
        num_toons = len(self.toons)
        return num_toons

    def owned_toons(self, star=1, exact=False):
        oper = '==' if exact  else '>='
        comp = '[toon for toon in self.toons if toon.star {} {}]'.format(oper, star)
        return eval(comp)

    @property
    def missing_toons(self):
        return [toon for toon in self.toons if toon.star == 0]


def main():
    user = Collections('w0m')
    print(user.num_toons)
    print(len(user.owned_toons(star=5, exact=True)))
    print(pprint(user.owned_toons(star=5, exact=True)))
    print(len(user.owned_toons()))


if __name__ == "__main__":
    main()
