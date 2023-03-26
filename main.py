import vk_api
from openpyxl import Workbook
from config import *

vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()

wb = Workbook()
ws = wb.active

out_name = input("Output file name ..xlsx")
domain = "forgottenfilms"
pages = vk.wall.get(domain=domain)['count'] // 20 + 1

for page in range(pages):
    print(str(round((page / pages) * 100, 2)) + "%")
    for post in vk.wall.get(domain=domain, offset=i * 20)["items"]:
        if not post['marked_as_ads']:
            ws.append(post["text"].split("\n"))

wb.save(f'{out_name}.xlsx')