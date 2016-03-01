import json
import requests

url = 'http://www.ionomicshub.org/arabidopsis/ajax/DataSearchJson.action'
#www.ionomicshub.org/arabidopsis/ajax/DataSearchJson.action?ATGNum=AT2G25360&Skip=3&Limit=1
#{'atgnum':'AT2G25360', 'skip':'3', 'limit':'1'}
def search(args):
	payload  = {'ATGNum': args['atgnum'], 'Skip': args['skip'], 'Limit': args['limit']}
	response = requests.get(url, params=payload)
	#print response.json()
	print response.text
    #print json.dumps({'obj': 1, 'args': args})
    #print "---"
    #print json.dumps({'obj': 2, 'args': args})
	