
import yaml
import json
from pprint import pprint as pp

f = open('yamlout.txt', 'r')
yaml_list = yaml.load(f)
f.close()
f = open('jsonout.txt', 'r')
json_list = json.load(f)

print('YAML List\n')
pp(yaml_list)
print('\nJSON List\n')
pp(json_list)

