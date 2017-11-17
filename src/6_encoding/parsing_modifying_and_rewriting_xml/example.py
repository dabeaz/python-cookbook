# example.py
#
# Example of reading an XML document, making changes, and writing it back out

from xml.etree.ElementTree import parse, Element
doc = parse('pred.xml')
root = doc.getroot()

# Remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# Insert a new element after <nm>...</nm>
nm_index = root.getchildren().index(root.find('nm'))

e = Element('spam')
e.text = 'This is a test'
root.insert(nm_index + 1, e)

# Write back to a file
doc.write('newpred.xml', xml_declaration=True)
