# encoding: utf-8
import json
import os
import pbs
import requests


GITHUB = 'https://api.github.com'
ORG = 'plone'
NUM_PAGES = range(3)  # XXX Fix me, use API to get the real number of pages


def clone_org_repos():
    print 'Cloning all the repos…'
    for page in NUM_PAGES:
        repos = requests.get('%s/orgs/%s/repos?per_page=100&page=%s' % (
            GITHUB, ORG, page + 1)).content
        for repo in json.loads(repos):
            name = repo['name']
            if os.path.exists(name):
                print '-> Updating %s' % name
                os.chdir(name)
                pbs.git('pull') 
                os.chdir('..')  # XXX Fix me, proper mult-plat parent dir?
            else:
                print '-> Cloning %s' % name
                pbs.git('clone', repo['git_url'])
    print 'Done, sleep tight.'
