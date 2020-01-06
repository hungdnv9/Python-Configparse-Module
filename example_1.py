# python3
import configparser
import os
import errno

config_file = './config.ini'
if not os.path.isfile(config_file):
	raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_file)	


config = configparser.ConfigParser()
config.read(config_file)

# Global
working_dir = config['Global']['working_dir']

# Section
sectionA_host = config['sectionA']['host']
sectionB_host = config['sectionB']['host']

# Interpolation
user1_home = config['info']['home_dir']

print (
	"working_dir: ",working_dir,
	"\nsectionA_host: ",sectionA_host,
	"\nsectionB_host: ",sectionB_host,
	"\nuser1_home: ",user1_home
)

