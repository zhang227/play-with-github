#!/usr/bin/env python
# coding=utf8
from api import *
import unittest


class TestApi(unittest.TestCase):

    def test_list_org_repos(self):
        l = list_org_repos('meetup')
        self.assertEqual(len(l), 133)
        self.assertEqual(l[0].name, 'python-api-client')

    def test_list_commits(self):
        l = list_commits('https://api.github.com/repos/meetup/snapup-android/commits')
        self.assertEqual(len(l), 126)
        self.assertEqual(l[0], '8cc3ce032ad798c8631593cdd8a271f0b9806e18')

    def test_get_contributor(self):
        c = get_contributor('https://api.github.com/repos/meetup/snapup-android/commits/8cc3ce032ad798c8631593cdd8a271f0b9806e18')
        self.assertEqual(c.login, 'n8han')
        self.assertEqual(c.additions, 2)
        self.assertEqual(c.deletions, 2)


if __name__ == '__main__':
    unittest.main()
