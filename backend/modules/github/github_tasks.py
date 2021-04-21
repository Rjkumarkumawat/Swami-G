#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import json
import requests
import re
from datetime import date, datetime

try:
    from factories._celery import create_celery
    from factories.application import create_application
    from celery.utils.log import get_task_logger
    celery = create_celery(create_application())
except ImportError:
    # This is to test the module individually, and I know that is piece of shit
    sys.path.append('../../')
    from factories._celery import create_celery
    from factories.application import create_application
    from celery.utils.log import get_task_logger
    celery = create_celery(create_application())

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logger = get_task_logger(__name__)

# Compatibility code
try:
    # Python 2: "unicode" is built-in
    unicode
except NameError:
    unicode = str


def findReposFromUsername(username):
	response = requests.get('https://api.github.com/users/%s/repos?per_page=100&sort=pushed' % username).text
	repos = re.findall(r'"full_name":"%s/(.*?)",.*?"fork":(.*?),' % username, response)
	nonForkedRepos = []
	for repo in repos:
		if repo[1] == 'false':
			nonForkedRepos.append(repo[0])
	return nonForkedRepos


def findEmailFromContributor(username, repo, contributor):
	response = requests.get('https://github.com/%s/%s/commits?author=%s' % (username, repo, contributor)).text
	latestCommit = re.search(r'href="/%s/%s/commit/(.*?)"' % (username, repo), response)
	if latestCommit:
		latestCommit = latestCommit.group(1)
	else:
		latestCommit = 'dummy'
	commitDetails = requests.get('https://github.com/%s/%s/commit/%s.patch' % (username, repo, latestCommit)).text
	email = re.search(r'<(.*)>', commitDetails)
	if email:
		email = email.group(1)
	return email


def findEmailFromUsername(username):
	repos = findReposFromUsername(username)
	for repo in repos:
		email = findEmailFromContributor(username, repo, username)
		if email:
			return email
	return False

@celery.task
def t_github(email, from_m="Initial"):
    """ Task of Celery that get info from github """

    if ("@" in email):
        username = email.split("@")[0]
    else:
        username = email

    email_github = findEmailFromUsername(username)

    req = requests.get("https://api.github.com/users/%s" % username)

    today = date.today()
    actual_year_from = date(today.year, today.month, 1)
    actual_year_to = date(today.year, today.month, today.day)
    previous_year_from = date(today.year - 1, today.month, 1)
    previous_year_to = date(today.year - 1, today.month, today.day)

    svg_req = "https://github.com/users/%s/contributions?from=%s&to=%s"
    svg_actual_r = requests.get(svg_req % (username, str(actual_year_from),
                                           str(actual_year_to)))
    svg_previous_r = requests.get(svg_req % (username, str(previous_year_from),
                                             str(previous_year_to)))
    # Change color of calendar
    # svg_actual = svg_actual_r.text.replace('ebedf0', '4d4d4d')
    # svg_previous = svg_previous_r.text.replace('ebedf0', '4d4d4d')
    svg_actual = svg_actual_r.text.replace('ebedf0', '295757')
    svg_previous = svg_previous_r.text.replace('ebedf0', '295757')

    # TODO : Many things
    # Use other API URLs

    # Raw Array
    raw_node = json.loads(unicode(req.text))

    # Total
    total = []
    total.append({'module': 'github'})
    total.append({'param': username})
    # Evaluates the module that executed the task and set validation
    if (from_m == 'Initial'):
        total.append({'validation': 'no'})
    else:
        total.append({'validation': 'soft'})

    if ('message' not in raw_node) or (raw_node['message'] != 'Not Found'):
        # Graphic Array
        graphic = []

        # Profile Array
        profile = []

        # Timeline Array
        timeline = []

        # Gather Array
        gather = []

        link = "Github"
        gather_item = {"name-node": "Github", "title": "Github",
                       "subtitle": "", "icon": "fab fa-github", "link": link}
        gather.append(gather_item)

        if (email_github):
            gather_item = {"name-node": "Gitemail", "title": "Git Email",
                           "subtitle": email_github, "icon": "fas fa-at",
                           "link": link}
            profile_item = {'email': email_github}
            profile.append(profile_item)
            gather.append(gather_item)
        if ('name' in raw_node):
            gather_item = {"name-node": "Gitname", "title": "Git Name",
                           "subtitle": raw_node['name'], "icon": "fas fa-user",
                           "link": link}
            profile_item = {'name': raw_node['name']}
            profile.append(profile_item)
            gather.append(gather_item)
        if ('email' in raw_node) and (raw_node['email'] is not None):
            gather_item = {"name-node": "GitEmail", "title": "Email",
                           "subtitle": raw_node['email'],
                           "icon": "fas fa-envelope",
                           "link": link}
            gather.append(gather_item)
            profile_item = {'email': raw_node['email']}
            profile.append(profile_item)
        if ('company' in raw_node) and (raw_node['company'] is not None):
            gather_item = {"name-node": "GitCompany", "title": "Company",
                           "subtitle": raw_node['company'],
                           "icon": "fas fa-building",
                           "link": link}
            gather.append(gather_item)
            profile_item = {'organization': raw_node['company']}
            profile.append(profile_item)
        if (('blog' in raw_node) and (raw_node['blog'] is not None) and
           (raw_node['blog'] != "")):
            gather_item = {"name-node": "GitBlog", "title": "Blog",
                           "subtitle": raw_node['blog'],
                           "icon": "fas fa-rss-square",
                           "link": link}
            gather.append(gather_item)
        if ('bio' in raw_node) and (raw_node['bio'] is not None):
            gather_item = {"name-node": "GitBio", "title": "Bio",
                           "subtitle": raw_node['bio'],
                           "icon": "fas fa-heart",
                           "link": link}
            gather.append(gather_item)
        if ('public_repos' in raw_node):
            gather_item = {"name-node": "GitRepos", "title": "Repos",
                           "subtitle": raw_node['public_repos'],
                           "icon": "fas fa-folder-open", "link": link}
            gather.append(gather_item)
        if ('public_gists' in raw_node):
            gather_item = {"name-node": "GitGists", "title": "Gists",
                           "subtitle": raw_node['public_gists'],
                           "icon": "fas fa-code", "link": link}
            gather.append(gather_item)
        if ('followers' in raw_node):
            gather_item = {"name-node": "GitFollowers", "title": "Followers",
                           "subtitle": raw_node['followers'],
                           "icon": "fas fa-users", "link": link}
            gather.append(gather_item)
        if ('following' in raw_node):
            gather_item = {"name-node": "GitFollowing", "title": "Following",
                           "subtitle": raw_node['following'],
                           "icon": "fas fa-users", "link": link}
            gather.append(gather_item)
        if ('id' in raw_node):
            gather_item = {"name-node": "GitId", "title": "Id",
                           "subtitle": raw_node['id'], "icon": "fas fa-info",
                           "link": link}
            gather.append(gather_item)
        if ('avatar_url' in raw_node):
            gather_item = {"name-node": "GitAvatar", "title": "Avatar",
                           "picture": raw_node['avatar_url'], "subtitle": "",
                           "link": link}
            gather.append(gather_item)
            profile_item = {'photos': [{"picture": raw_node['avatar_url'],
                                        "title": "Github"}]}
            profile.append(profile_item)
        if ('location' in raw_node) and (raw_node['location'] is not None):
            profile_item = {'location': raw_node['location']}
            profile.append(profile_item)
        if ('created_at' in raw_node) and (raw_node['created_at'] is not None):
            ctime = datetime.strptime(raw_node['created_at'],
                                      "%Y-%m-%dT%H:%M:%SZ")
            timeline_item = {'date': ctime.strftime("%Y/%m/%d %H:%M:%S"),
                             'action': 'Github : Create Account',
                             'icon': 'fab fa-github'}
            timeline.append(timeline_item)
        if ('updated_at' in raw_node) and (raw_node['updated_at'] is not None):
            mtime = datetime.strptime(raw_node['updated_at'],
                                      "%Y-%m-%dT%H:%M:%SZ")
            timeline_item = {'date': mtime.strftime("%Y/%m/%d %H:%M:%S"),
                             'action': 'Github : Update Account',
                             'icon': 'fab fa-github'}
            timeline.append(timeline_item)

        # Please, respect the order of items in the total array
        # Because the frontend depend of that (By now)
        total.append({'raw': raw_node})
        graphic.append({'github': gather})
        graphic.append({'cal_actual': svg_actual})
        graphic.append({'cal_previous': svg_previous})
        total.append({'graphic': graphic})
        total.append({'profile': profile})
        total.append({'timeline': timeline})

    return total


def output(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    email = sys.argv[1]
    result = t_github(email)
    output(result)
