import yaml
import os


''' CHANGE THIS FOR VM, Top For VM, Bottum For Local'''

dir_path = os.path.dirname(os.path.realpath(__file__))
input = dir_path+"/credentials.txt"

with open(input, 'r') as f:
    doc = yaml.safe_load(f)

fburl = doc["fogbugz"]["url"]
fbuser = doc["fogbugz"]["username"]
fbpassword = doc["fogbugz"]["password"]

maximum = doc["maxresult"]

f.close()