from distutils.core import setup
setup(
	name='qradarapi',
	packages = ['qradarapi'],
	version = '0.1',
	description = 'Python interface to the QRadar API',
	author = 'Mike Patterson',
	author_email = 'mike.patterson@uwaterloo.ca',
	keywords = ['qradar'],
	classifiers = [],
	license = 'BSD',
	install_requires = [
		"pyopenssl",
		"requests",
		],
)
