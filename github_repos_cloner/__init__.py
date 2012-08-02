# encoding: utf-8
import json
import os
import pbs
import requests
import sys


GITHUB = 'https://api.github.com'
NUM_PAGES = range(3)  # XXX Fix me, use API to get the real number of pages
ACCT_TYPE = (
    'orgs',
    'user',
)


def clone_repos():
    print 'Cloning all the repos…'

    user_or_org = sys.argv[1]

    for account_type in ACCT_TYPE:
        for page in NUM_PAGES:
            repos = requests.get('%s/%s/%s/repos?per_page=100&page=%s' % (
                GITHUB, account_type, user_or_org, page + 1)).content
            for repo in json.loads(repos):
                name = repo['name']
                if name == 'org_repos_cloner':  # Don't clone the cloner, man
                    continue
                if os.path.exists(name):
                    print '-> Updating %s' % name
                    os.chdir(name)
                    pbs.git('pull') 
                    os.chdir('..')  # XXX Fix me, proper mult-plat parent dir?
                else:
                    print '-> Cloning %s' % name
                    pbs.git('clone', repo['git_url'])
    print 'Done, sleep tight.'
