from xml.etree import ElementTree as ET


# Make a beautiful heading

def heading(func):
    def decorate(text):
        print(end="\n"*2)
        print("#"*(int(len(text))+4))
        print("# " + str(func(text)) + " #")
        print("#"*(int(len(text))+4), end="\n"*2)
        
    return decorate


# Create the xml object
tree = ET.parse("data-text.xml")
root = tree.getroot()


# Print the tag name of the root element

@heading
def hroot(text):
    return text
hroot("ROOT")
print(root)


@heading
def childelement(text):
    return text


childelement("CHILDELEMENT")
print(list(root))


@heading
def hdata(text):
    return text

hdata("DATA")
data = root.find("data")
print(list(data))

