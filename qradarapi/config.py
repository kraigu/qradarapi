import os
import stat
import sys
import logging

from ConfigParser import *
import qradarapi.settings as qrsettings

logging.basicConfig()
logger = logging.getLogger(__name__)

class QRadarConnectConfig:
	def __init__(self, filename=qrsettings.default_filename):
		self._cfgfile = None
		if os.path.exists(filename):
			self._cfgfile = filename
		elif os.path.exists(os.path.join(os.path.expanduser("~"), filename)):
			self._cfgfile = os.path.join(os.path.expanduser("~"), filename)
		else:
			# rude!
			logging.critical("You need a config file")
			sys.exit(2)

		if self._cfgfile:
			self._cfgfile = os.path.realpath(self._cfgfile)
			self._cfgparse = ConfigParser(qrsettings.defaults)
			self._cfgparse.read(self._cfgfile)
		else:
			# also rude!
			logging.critical("Something went wrong with parsing config file")
			sys.exit(2)

	def get_config_filename(self):
		return self._cfgfile

	def get_config(self):
		return self._cfgparse

	def get_auth(self):
		return (self._cfgparse.get('info', 'apikey'))

	def get_hostname(self):
		return self._cfgparse.get('info', 'hostname')

	def get_certbundlefile(self):
		return self._cfgparse.get('info','certbundlefile')
