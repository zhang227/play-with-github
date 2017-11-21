#!/usr/bin/env python
# coding=utf8
from api import *

REPOS = 'meetup'

if __name__ == '__main__':
    repos_list = list_org_repos(REPOS)
    star_list = sorted(repos_list, key=lambda x: -x.stargazers_count)[:3]
    with open('result.txt', 'w') as f:
        f.write('repos based on stars:\n')
        for i in star_list:
            f.write('%s\t%d\n' % (i.name, i.stargazers_count))

        f.flush()
        f.write('\nrepos based on watch:\n')
        watch_list = sorted(repos_list, key=lambda x: -x.watchers_count)[:3]
        for i in watch_list:
            f.write('%s\t%d\n' % (i.name, i.watchers_count))

        f.flush()
        f.write('\nrepos based on fork:\n')
        fork_list = sorted(repos_list, key=lambda x: -x.forks_count)[:3]
        for i in fork_list:
            f.write('%s\t%d\n' % (i.name, i.forks_count))

        f.flush()

        contributors = {}
        for repo in repos_list[:5]:
            commits = list_commits(repo.commits_url)
            for commit in commits[:10]:
                try:
                    cur = get_contributor(repo.commits_url.replace('{/sha}', '/' + commit))
                    if cur.login in contributors:
                        cur.additions += contributors[cur.login].additions
                        cur.deletions += contributors[cur.login].deletions
                        cur.commits += 1
                    contributors[cur.login] = cur
                except Exception as e:
                    print(e)
        f.flush()

        f.write('\nunique contributors:\n')
        for c in contributors.keys():
            f.write(c + '\t')
        f.write('\n')
        f.flush()

        top_cons = sorted(contributors.values(), key=lambda x: -x.additions)[:3]
        f.write('\ncontributors based on additions:\n')
        for c in top_cons:
            f.write('%s\t%d\n' % (c.login, c.additions))
        f.flush()

        top_cons = sorted(contributors.values(), key=lambda x: -x.deletions)[:3]
        f.write('\ncontributors based on deletions:\n')
        for c in top_cons:
            f.write('%s\t%d\n' % (c.login, c.deletions))
        f.flush()

        top_cons = sorted(contributors.values(), key=lambda x: -x.commits)[:3]
        f.write('\ncontributors based on number of commits:\n')
        for c in top_cons:
            f.write('%s\t%d\n' % (c.login, c.commits))
    print('\nFinish.\n')
