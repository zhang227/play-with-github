#!/usr/bin/env python
# coding=utf8


class Repos:

    def __init__(self, json_data):
        self.name = json_data['name']
        self.stargazers_count = json_data['stargazers_count']
        self.watchers_count = json_data['watchers_count']
        self.forks_count = json_data['forks_count']
        self.commits_url = json_data['commits_url']

    def __str__(self):
        return 'name=%s,stargazers_count=%d,watchers_count=%d,forks_count=%d,commits_url=%s' \
               % (self.name, self.stargazers_count, self.watchers_count, self.forks_count,
                  self.commits_url)


class Contributor:

    def __init__(self, json_data):
        self.login = json_data['committer']['login']
        self.additions = json_data['stats']['additions']
        self.deletions = json_data['stats']['deletions']
        self.commits = 1

    def __eq__(self, other):
        return self.login == other.login

    def __hash__(self):
        return self.login
