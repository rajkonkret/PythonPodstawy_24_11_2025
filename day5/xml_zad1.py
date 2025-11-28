# xml
# <ExchangeRatesSeries xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
# <Table>A</Table>
# <Currency>bat (Tajlandia)</Currency>
# <Code>THB</Code>
# <Rates>
# <Rate>
# <No>231/A/NBP/2025</No>
# <EffectiveDate>2025-11-28</EffectiveDate>
# <Mid>0.1138</Mid>
# </Rate>
# </Rates>
# </ExchangeRatesSeri

from xml.dom import minidom

root = minidom.Document()  # <?xml version="1.0" ?>
xml = root.createElement('root')  # # <root>
root.appendChild(xml)

productChild = root.createElement('product')  # # 	<product
productChild.setAttribute("name", "RAJ")  # name="RAJ"/>
xml.appendChild(productChild)

xml_str = root.toprettyxml(indent='\t')
print(xml_str)
# <?xml version="1.0" ?>
# <root>
# 	<product name="RAJ"/>
# </root>

with open('dane_xml.xml', "w") as f:
    f.write(xml_str)