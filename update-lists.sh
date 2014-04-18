#!/bin/bash
./get-russian-blacklist.py | tee russian-blacklist-prosecutor-general-office.csv 
./get-russian-blacklist.py -j | python -mjson.tool | tee russian-blacklist-prosecutor-general-office.json
./get-russian-blacklist.py -y | tee russian-blacklist-prosecutor-general-office.yaml
