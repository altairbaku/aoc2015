import re
import json
with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    json_input = line.strip()

numbers = [int(d) for d in re.findall(r'-?\d+',json_input)]
print(sum(numbers))

def sum_p2(json_packet):
    json_sum = 0
    if type(json_packet) is dict and 'red' not in json_packet.values():
        for k,v in json_packet.items():
            if type(v) is list:
                json_sum += sum_p2(v)
            elif type(v) is int:
                json_sum += v
            elif type(v) is dict:
                json_sum += sum_p2(v)
    if type(json_packet) is list:
        for item in json_packet:
            if type(item) is dict:
                if "red" in item.values():
                    continue
                else:
                    json_sum += sum_p2(item)
            elif type(item) is list:
                json_sum += sum_p2(item)
            elif type(item) is int:
                json_sum += item

    return json_sum

y = json.loads(json_input)
print(sum_p2(y))
