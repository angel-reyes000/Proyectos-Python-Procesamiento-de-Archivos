import xml.etree.ElementTree as et
import xml.dom.minidom

class products:
    def __init__(self):
        self.product = et.SubElement(category, "product")
        self.type = et.SubElement(self.product, "type")
        self.producer = et.SubElement(self.product, "producer")
        self.price = et.SubElement(self.product, "price")
        self.currency = et.SubElement(self.product, "currency")

root = et.Element("shop")
category = et.SubElement(root, "category", {"name" : "Vegan Products"})

pro1 = products()
pro2 = products()
pro3 = products()

pro1.product.set("name", "Good Morning Sunshine")
pro1.type.text = "cereals"
pro1.producer.text = "OpenEDG Testing Service"
pro1.price.text = "9.90"
pro1.currency.text = "USD"

pro2.product.set("name", "Spaghetti Veganietto")
pro2.type.text = "pasta"
pro2.producer.text = "Programmers Eat Pasta"
pro2.price.text = "15.49"
pro2.currency.text = "EUR"

pro3.product.set("name", "Fantastic Almond Milk")
pro3.type.text = "beverages"
pro3.producer.text = "Drinks4Coders Inc."
pro3.price.text = "19.75"
pro3.currency.text = "USD"

xml_str = et.tostring(root, encoding="UTF-8")
dom = xml.dom.minidom.parseString(xml_str)
print(dom.toprettyxml(indent="  "))

tree = et.ElementTree(root)

#tree.write(r"C:\Users\Luis Reyes\Downloads\shop.xml.txt", "UTF-8", True)