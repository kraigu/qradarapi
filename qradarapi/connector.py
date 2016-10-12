import requests
import logging
import urllib

class QRConnector():
	def __init__(self, server='localhost', auth='0', certbundlefile=None):
		self.server = server
		self.auth = auth
		self.certbundlefile = certbundlefile
		self.session = requests.Session()
		self.session.mount('https://', 3)

	def __call__(self):
		return self

	# Method to submit a properly-formed request with required headers, as well as any extras
	# Things will not go well if somebody passes SEC header themselves, but what can you do?
	# You can call this directly if a more specific helper method is missing, like this:
	# r = cobj.qrrequest(cobj.server, cobj.auth, 'system/servers', 'GET')
	# r.json()
	def qrrequest(self, requrl=None, http_method=None, extra_headers=None):
		#print ('Trying to connect to {}'.format(self.server))
		#print ('Arguments to qrrequest: {}\t{}\n{}'.format(requrl, http_method, extra_headers))
		ourl = "https://{}/api/{}".format(self.server, requrl)
		#print('Requesting {} URL {}'.format(http_method,ourl))
		if extra_headers is None:
			extra_headers = {}
		extra_headers['SEC'] = self.auth
		#print extra_headers
		if http_method == "GET":
			return requests.get(ourl, headers=extra_headers, verify=self.certbundlefile)
		elif http_method == "POST":
			return requests.post(ourl, headers=extra_headers, verify=self.certbundlefile)
		else:
			# this is better handled as an exception I guess
			return None

	# Return an unsorted list of servers in this cluster
	def list_servers(self):
		return self.qrrequest('system/servers','GET')

	def list_arieldbs(self, range=None):
		if range is None:
			return self.qrrequest('ariel/databases', 'GET')
		else:
			rangestr = {'Range': "items=".format(range)}
			print rangestr
			return self.qrrequest('ariel/databases', 'GET', rangestr)

	def list_searches(self, range=None):
		if range is None:
			return self.qrrequest('ariel/searches','GET')
		else:
			rangestr = {'Range': "items=".format(range)}
			print rangestr
			return self.qrrequest('ariel/searches', 'GET', rangestr)

	def get_search(self, searchid=None):
		# TODO: check to ensure search has actually completed...
		sstring = "ariel/searches/" + searchid
		r = self.qrrequest(sstring, 'GET')
		return r

	def get_search_results(self, searchid=None):
		# TODO: check to ensure search has actually completed... or else use get_search for that.
		sstring = "ariel/searches/" + searchid + "/results"
		r = self.qrrequest(sstring, 'GET')
		return r

	def start_search(self, aqlstr=None):
		apipath = "ariel/searches?"
		sexp = {'query_expression': aqlstr}
		sstring = '{}{}'.format(apipath,urllib.urlencode(sexp))
		r = self.qrrequest(sstring, 'POST')
		return r
