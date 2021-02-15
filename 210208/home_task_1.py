import re

import requests

RE_CSV_FILE = re.compile(r'"([^"А-Яа-яЁё]+\.)"')

file_name = 'text.csv'
request_csv = 'text.csv'

response = requests.get(request_csv)
content = response.content.splitlines()


parsed = RE_CSV_FILE.findall(content)
parsed = filter(lambda x: x.endswith('.csv'), parsed)
print(type(parsed))
print(len(list(parsed)))
print(*parsed, sep='\n\n')
csv_gen = (row for row in open(file_name))