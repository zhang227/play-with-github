#!/usr/bin/env python
# coding=utf8
import requests
from model import Repos, Contributor

__ACCESS_TOKEN = '7754abc4f99124671f1d5856eddc24c882d8a9dc'


def list_all(url):
    page = 1
    res = []
    while True:
        u = '%s?page=%d&per_page=100&access_token=%s'
        r = requests.get(u % (url, page, __ACCESS_TOKEN))
        print(u % (url, page, __ACCESS_TOKEN))
        r = r.json()
        if not r:
            break
        res += r
        page += 1
        #print(r)
    return res


def list_org_repos(org):
    # issue the HTTP request
    url = 'https://api.github.com/orgs/%s/repos' % org
    return [Repos(i) for i in list_all(url)]


def list_commits(url):
    url = url.replace('{/sha}', '')
    return [i['sha'] for i in list_all(url)]


def get_contributor(url):
    url = url + '?access_token=' + __ACCESS_TOKEN
    print(url)
    data = requests.get(url).json()
    print(data)
    return Contributor(data)

