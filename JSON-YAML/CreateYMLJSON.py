import yaml
import json
import pprint

my_list = [ {
 "interfaces": {
     "FastEthernet0/1": { 
       "description": "Test Interface",
       "ip": "10.232.212.1",
       "mask": "255.255.255.0",
     }, 
     "FastEthernet0/2": {
        "description": "Test2 Interface",
        "ip": "10.232.213.1",
        "mask": "255.255.255.0",
     }
    }
  },
  { "routing_protocols": ["bgp","ospf"] }
]

f = open('jsonout.txt', 'w')
json.dump(my_list, f)
f.close()

f = open('yamlout.txt', 'w')
f.write(yaml.dump(my_list, default_flow_style=False))
f.close()
