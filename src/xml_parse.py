import xml.etree.ElementTree as etree

tree = etree.parse("tmp/time_series_patient.xml")
elem = tree.getroot()

#print elem.find(".//Sex").text


def iterparent(elem):
    for parent in elem.getiterator():
        for child in parent:
            for gson in child:
            	yield parent, child, gson

for p,c,g in iterparent(elem):
    print '----'
    print c.tag
    print g.tag
    print g.tag + "=" +  g.text
