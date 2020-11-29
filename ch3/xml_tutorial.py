xml_text = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""

from xml.etree import ElementTree as ET

# Read the xml text directly from a string
root = ET.fromstring(xml_text)

# Print some data about the xml object
print("Name of the root tag: " + str(root.tag))
print("Attributes of the root tag (none here): " + str(root.attrib))

# Iterate over the child items under the root element.
print("#"*80)
for child in root:
    print(child.tag, child.attrib)

# Accesing child elements with an index.
print(root[0].attrib["name"], root[0][1].text)

# Iterate recursively over child item.
print("#"*80)
for neighbor in root.iter("neighbor"):
    print(neighbor.attrib)

for rank in root.iter("rank"):
    print(rank.text)

for country in root.iter("country"):
    print(country.attrib["name"])

# Find direct child item and get text and attribute values.
for country in root.findall("country"):
    name = country.get("name")
    rank = country.find("rank").text
    print(f"{name}: {rank}")


# Populate a Python dictionary.
country_names_keys = [country.attrib["name"] for country in root]
print("#"*80)
print(country_names_keys)
country_rank_values = [[rank.text for rank in country.findall("rank")] for country in root]
print("#"*80)
print(country_rank_values)
print("#"*80)
for country in root:
    #print(country)
    for rank in country.findall("rank"):
        print(rank.text)

print("#"*80)
country_rank_values_2 = [rank.text for country in root for rank in country.findall("rank")]
print(country_rank_values_2)
test_list = []
for country in root:
    for rank in country.findall("rank"):
        test_list.append(rank.text)

print(test_list)

csv_dict = zip(country_names_keys, country_rank_values_2)
print(dict(csv_dict))

# Export the extracted data to a csv file.

