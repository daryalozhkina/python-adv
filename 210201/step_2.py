import re

import requests

# RE_XLS_FILE = re.compile(r'href=".+"')
# RE_XLS_FILE = re.compile(r'href="[^"]+\.xls"')
RE_XLS_FILE = re.compile(r'href="([^"]+\.xls)"')

request_url = 'https://kpk.kss45.ru/учебная-работа/расписание_пар.html'

response = requests.get(request_url)
content = response.content.decode(encoding=response.encoding)

parsed = RE_XLS_FILE.findall(content)
# parsed = filter(lambda x: x.endswith('.xls"'), parsed)
print(len(parsed))
print(*parsed, sep='\n\n')
