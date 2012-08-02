import json
import requests


GITHUB = 'https://api.github.com'
ORG = 'plone'
NUM_PAGES = range(3)  # XXX Fix me, use API to get the real number of pages


def clone_org_repos():
    for page in NUM_PAGES:
        repos = requests.get('%s/orgs/%s/repos?per_page=100&page=%s' % (
            GITHUB, ORG, page + 1)).content
        for repo in json.loads(repos):
            print repo['git_url']
