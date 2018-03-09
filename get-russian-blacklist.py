#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
import sys
import json
import tablib
import argparse

# parse args
parser = argparse.ArgumentParser(description='Retrieve all URLs that are in the Russian black list that have been added by the Prosecutor Generals Office.')
parser.add_argument('-c', '--csv', help='retrieve csv', action='store_true')
parser.add_argument('-y', '--yaml', help='retrieve yaml', action='store_true')
parser.add_argument('-j', '--json', help='retrieve json', action='store_true')
parser.add_argument('-a', '--all', help='get all blacklist (not just Prosecutor General Office)', action='store_true')
args = parser.parse_args()

# hit zapret api
api_url = "http://api.antizapret.info/all.php?type=json"
r = requests.get(api_url)

# can add more orgs to the dictionary if you want
if sys.version_info[0] <= 2:
    interesting_orgs = [u"Генпрокуратура"]
elif sys.version_info[0] >= 3:
    interesting_orgs = ["Генпрокуратура"]

j = json.loads(r.text)
result = j['register']

headers = ('url', 'ip', 'added_time')
data = tablib.Dataset(headers=headers)
for entry in result:
    if args.all:
        data.append((entry['url'], entry['ip'], entry['includeTime']))
    elif entry['org'] in interesting_orgs:
        data.append((entry['url'], entry['ip'], entry['includeTime']))

if args.csv:
    print(data.csv)
elif args.json:
    print(data.json)
elif args.yaml:
    print(data.yaml)
else:
    print(data.csv)
