import pandas as pd
import requests
from bs4 import BeautifulSoup
URL = "https://strftime.org/"
respone = requests.get(url=URL)
soup = BeautifulSoup(
    markup=respone.text,
    features="html.parser",
)
table_tag = soup.find(name="table")
thead_tag = table_tag.find(name="thead")
th_tags = thead_tag.find_all(name="th")
table_header = [th_tag.text for th_tag in th_tags]
tbody_tag = table_tag.find(name="tbody")
tr_tags = tbody_tag.find_all(name="tr")
# print(tr_tags)
row_list = list()
for tr_tag in tr_tags:
    # print(tr_tag)
    td_tags= tr_tag.find_all(name="td")
    # print(td_tags)
    row = [td_tag.text for td_tag in td_tags]
    # print(row)
    row_dict = {
        table_header[0]:row[0],
        table_header[1]:row[1],
        table_header[2]:row[2],
    }
    row_list.append(row_dict)
# print(row_list)
df = pd.DataFrame(data=row_list)
print(df)