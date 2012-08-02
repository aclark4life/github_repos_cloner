# encoding: utf-8
import json
import os
import pbs
import requests
import sys


GITHUB = 'https://api.github.com'
NUM_PAGES = range(3)  # XXX Fix me, use API to get the real number of pages
ACCT_TYPE = {
    'org': '%s/orgs/%s/repos?per_page=100&page=%s',
    'user': '%s/users/%s/repos?per_page=100&page=%s',
}


def clone_repos():
    print 'Cloning all the repos…'

    user_or_org = sys.argv[1]

    for account_type in ACCT_TYPE:
        for page in NUM_PAGES:
            repos = requests.get(ACCT_TYPE[account_type] % (GITHUB,
                user_or_org, page + 1)).content
            repos = json.loads(repos)
            if 'message' in repos:  # gh error
                break
            for repo in repos:
                name = repo['name']
                if os.path.exists(name):
                    os.chdir(name)
                    try:
                        print '-> Updating %s' % name
                        pbs.git('pull')
                    except:
                        print '-> Updating %s, git pull failed!' % name
                    os.chdir('..')  # XXX Fix me, proper mult-plat parent dir?
                else:
                    print '-> Cloning %s' % name
                    pbs.git('clone', repo['git_url'])
    print 'Done, sleep tight.'
