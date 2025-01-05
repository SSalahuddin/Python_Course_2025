import xml.etree.ElementTree as ET

# Creating an XML file
data = ET.Element('data')
person = ET.SubElement(data, 'person')
person.set('id', 'ABC123')
ET.SubElement(person, 'name').text = 'Ahmad'
ET.SubElement(person, 'age').text = '25'
ET.SubElement(person, 'city').text = 'Peshawar'

person = ET.SubElement(data, 'person')
person.set('id', 'ABC124')
ET.SubElement(person, 'name').text = 'Ali'
ET.SubElement(person, 'age').text = '20'
ET.SubElement(person, 'city').text = 'Kabul'

tree = ET.ElementTree(data)
tree.write('data.xml')

# Reading from an XML file
tree = ET.parse('data.xml')
root = tree.getroot()
for person in root.findall('person'):
    id = person.get('id')
    name = person.find('name').text
    age = person.find('age').text
    city = person.find('city').text
    print(f'{name}, {age}, {city}')
