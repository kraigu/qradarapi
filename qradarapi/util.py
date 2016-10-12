import qradarapi.config as qrconfig
import qradarapi.connector as qrconnector
import qradarapi.settings as qrsettings

def connect(config_file=qrsettings.default_filename):
	conf = qrconfig.QRadarConnectConfig(filename = config_file)
	connect = qrconnector.QRConnector( conf.get_hostname(), conf.get_auth(), conf.get_certbundlefile() )
	return connect