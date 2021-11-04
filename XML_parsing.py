import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree
import pandas as pd

xml_file = 'C:/Users/kakaopaysec/Desktop/Trademark/apc18840407-20201231-70.xml'
doc = ET.parse(xml_file)

root = doc.getroot()

# for child in root.findall("./application-information/file-segments"):
#     print(child.tag, child.attrib)

temp = []
# for child in root.find('application-information').find('file-segments').find('action-keys').find('case-file').find('case-file-header'):
#

# print(temp[4])

date = []
for child in root.find('application-information').find('file-segments').find('action-keys').findall('case-file'):
    date.append(child.find('transaction-date').text)

# print(date)

mark = []
for child in root.find('application-information').find('file-segments').find('action-keys').findall('case-file'):
    mark2 = []
    for ch in child.find('case-file-header').findall('mark-identification'):
        mark2.append(ch.text)
    mark.append(mark2)

owner = []
for child in root.find('application-information').find('file-segments').find('action-keys').findall('case-file'):
    try:
        owner.append(child.find('case-file-owners').find('case-file-owner').find('party-name').text)
    except:
        owner.append(0)

# print(owner)

print(len(date), len(mark), len(owner))

dict = {'date':date,
        'name':mark,
        'owner_name':owner}

df = pd.DataFrame(dict)
print(df)

# print(mark)