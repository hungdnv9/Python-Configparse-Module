# python3
import configparser

config = configparser.ConfigParser()

config.add_section('SectionI')
config['SectionI']['name'] = 'hung'
config['SectionI']['age'] = '23'

output_file =  './output_conf.ini'
with open(output_file, 'w') as f:
	config.write(f)


