import ez_setup
ez_setup.use_setuptools

from setuptools import setup, find_packages
#from setuptools import setup, find_packages, Extension
import warnings
warnings.filterwarnings("ignore", "Unknown distribution option")

#from phyghtmap import __version__

setup(name="phyghtmap",
	version="1.46",
	packages = find_packages(),
	description="OSM contour lines creator.",
	include_data_files=True,
	author="Adrian Dempwolff",
	author_email="adrian.dempwolff@urz.uni-heidelberg.de",
	url="http://katze.tfiu.de/projects/phyghtmap/",
	long_description="""phyghtmap creates openstreetmap suitable contour lines from NASA SRTM data.""",
	license="GPLv2+",
	#ext_modules=[
		#Extension("phyghtmap.pbfint", ["phyghtmap/pbfintmodule.c"])
	#],
	entry_points = {
		'console_scripts': [
			'phyghtmap = phyghtmap.main:main',
		],
	},
	)

