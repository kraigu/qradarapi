#!/usr/bin/env python

import qradarapi
from time import sleep

cobj = qradarapi.connect()
print "Server: {}\nKey: {}".format(cobj.server, cobj.auth)
r = cobj.list_servers()

for k in r.json():
	print("{}\t{}\t{}").format(k['status'],k['hostname'],k['private_ip'])

r = cobj.list_arieldbs()
print r.json()

r = cobj.list_searches()
searches = r.json()
for k in searches:
	r = cobj.get_search(k)
	t = r.json()
	if t['status'] == "COMPLETED":
		print "{}\t{}\t{}".format(k, t['data_total_size'], t['save_results'])

r = cobj.start_search("select * from events where userName like 'mpatters%' last 2 days")
sstring = r.json()['search_id']
scomplete = False
while not(scomplete):
	r = cobj.get_search(sstring)
	if r.json()['status'] == "EXECUTE":
		time.sleep(3)
	else:
		scomplete = True
# This is not to say that the search completed successfully, so some rudimentary checking		
if r.json()['status'] == "COMPLETED":
	r = cobj.get_search_results(sstring)
	l = r.json()
	for k in l['events']:
		print "{}\t{}  {}\t{}\t{}\t{}".format(k['logsourceid'],k['username'],k['qid'],k['sourceip'],k['destinationip'],k['starttime'])
else:
	print "Something went wrong, search {} did not complete:\n{}".format(sstring,r.json['status'])
