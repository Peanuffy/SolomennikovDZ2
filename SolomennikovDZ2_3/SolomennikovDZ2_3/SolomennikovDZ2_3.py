import json
import msgpack
import os

with open('third_task.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

aggregated_data = {}

for product in products:
    product_name = product['name'] 
    price = product['price'] 

    if product_name not in aggregated_data:
        aggregated_data[product_name] = {
            'prices': []
        }

    aggregated_data[product_name]['prices'].append(price)

for product_name, data in aggregated_data.items():
    prices = data['prices']

    average_price = sum(prices) / len(prices)
    max_price = max(prices)
    min_price = min(prices)

    aggregated_data[product_name] = {
        'average_price': average_price,
        'max_price': max_price,
        'min_price': min_price,
    }

with open('third_task_results.json', 'w', encoding='utf-8') as f:
    json.dump(aggregated_data, f, ensure_ascii=False, indent=4)

with open('third_task_results.msgpack', 'wb') as f:
    msgpack.dump(aggregated_data, f)

json_size = os.path.getsize('aggregated_data.json')
msgpack_size = os.path.getsize('aggregated_data.msgpack')

print(f'JSON file size: {json_size / 1024:.2f} KB')
print(f'Msgpack file size: {msgpack_size / 1024:.2f} KB')
