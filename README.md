What Is It?
-----------

Gets a simple dump of the Russian Federal Black List of blocked sites from the excellent [antizapret site](http://antizapret.info/)
in a variety of formats (csv, json, yaml).  By default gets only sites that were added by the Prosecutors General Office since this
content is most often political in nature.  

Install
-------------

Python interpreter 2.6+

To get required libraries simply do:

	sudo pip install requests tablib json


Usage
-------

To retrieve just sites added by the Prosecutor General as csv:

	./get-russian-blacklist.py

To retrieve whole black list as a csv:

	./get-russian-blacklist.py -a

To get whole list in json:
	
	./get-russian-blacklist.py -a -j

For more help

	./get-russian-blacklist.py -h


Data
----

Along with code included is also the Russian Blacklist of URLs added by the
Prosecutor General Office in CSV, JSON and YAML.  These sites are *blocked
sites* so they may contain offensive content.

License
--------

This data is provided under Creative Commons Attribution-ShareAlike 4.0
International (CC BY-SA 4.0) which is summarized
[here](http://creativecommons.org/licenses/by-sa/4.0/) and available in full
[here](http://creativecommons.org/licenses/by-sa/4.0/legalcode)

