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
