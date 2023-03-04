import redis
import json


red = redis.Redis(
    host='redis-15889.c251.east-us-mz.azure.cloud.redislabs.com',
    port=15889,
    password='tFa3IZZIFvWC09y854ruhsrG840nyWfQ'
)
cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break
