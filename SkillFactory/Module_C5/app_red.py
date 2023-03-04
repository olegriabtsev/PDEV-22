import redis
import json


red = redis.Redis(
    host='redis-15889.c251.east-us-mz.azure.cloud.redislabs.com',
    port=15889,
    password='tFa3IZZIFvWC09y854ruhsrG840nyWfQ'
)
# dict1 = {
#     'key1': 'value1',
#     'key2': 'value2'
# }
# red.set('dict1', json.dumps(dict1))
# converted_dict = json.loads(red.get('dict1'))
red.delete('key')

print(red.get('key'))
