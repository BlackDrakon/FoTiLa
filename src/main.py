import json

print("Hi I am FoTiLa")

config_src = {'save path': 'value1', 'key2': {'key3': 'value2','key5': 'value4' }}

print(config_src)

#with open('config.json', 'w') as f:
#    json.dump(config_src, f)
    
with open('config.json', 'r') as f:
    config = json.load(f)
    
config['key3'] = 'new_value'


#write it back to the file
with open('config.json', 'w') as f:
    json.dump(config, f)
    
print(config)