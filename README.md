# Purpose
- Read from config file
- Write config to file

## Case 1: Read from config file
```sh
$ python3 example_1.py 
working_dir:  /data/my_work 
sectionA_host:  sectiona.com 
sectionB_host:  sectionb.com 
user1_home:  /home/Jano
```

## Case 2: Write config to file
```sh
$ python write_config_to_file.py
$ cat output_conf.ini 
[SectionI]
name = hung
age = 23
```
