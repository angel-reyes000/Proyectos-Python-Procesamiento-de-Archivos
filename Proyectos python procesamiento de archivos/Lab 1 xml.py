import xml.etree.ElementTree

class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, celsius):
        F = (9/5 * celsius) + 32
        return F
    
class ForecastXmlParser(TemperatureConverter):
    def __init__(self):
        self.tree = xml.etree.ElementTree.parse("C:\\Users\\Luis Reyes\\Downloads\\forecast.xml")
        self.root = self.tree.getroot()

    def dias_semana(self):
        dias = []
        for hijo in self.root.findall("item"):
            dias.append(hijo.find("day").text + ":")
        return dias
    
    def grados_celsius(self):
        temperaturas = []
        for temperatura in self.root.findall("item"):
            tem = temperatura.find("temperature_in_celsius").text + " Celsius"
            temperaturas.append(tem)
        return temperaturas
    
    def grados_fahrenheit(self):
        temperaturas = []
        for temperatura in self.root.findall("item"):
            tem = temperatura.find("temperature_in_celsius").text
            numero = float(tem)
            operacion = TemperatureConverter.convert_celsius_to_fahrenheit(self, numero)
            resultado = str(round(operacion, 1))
            temperaturas.append(resultado)
        for q in range(len(temperaturas)):
            temperaturas[q] += " Fahrenheit"
        return temperaturas
    
    def datos_completos_temperaturas(self):
        temperaturas = []
        for dia, celsius, fahrenheit in zip(self.dias_semana(), self.grados_celsius(), self.grados_fahrenheit()):
            diario =  dia + " " + celsius + ", " + fahrenheit
            temperaturas.append(diario)
        return "\n".join(temperaturas)

Datos_de_clima = ForecastXmlParser()
print(Datos_de_clima.datos_completos_temperaturas())

