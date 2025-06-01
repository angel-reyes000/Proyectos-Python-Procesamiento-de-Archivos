import csv 

class PhoneContacts:
    def __init__(self, name, phone):
        self._name=name
        self._phone=phone

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name
        else:
            raise ValueError("Invalid name")
    
    @name.deleter
    def name(self):
        print("Name deleted")
        del self._name

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, new_phone):
        self._phone = new_phone

    @phone.deleter
    def phone(self):
        print("Phone deleted")
        del self._phone

class Phone:
    def __init__(self):
        self.file = open(r"C:\Users\Luis Reyes\Downloads\contacts.csv", "r", newline="")
        reader = csv.DictReader(self.file, delimiter=",")
        self._contacts = reader

    @property
    def contacts(self):
        return self._contacts
    
    @contacts.setter
    def contacts(self, new_contacts):
        self._contacts = new_contacts

    @contacts.deleter
    def contacts(self):
        print("Contacts deleted")
        del self._contacts

    def load_contacts_from_csv(self):
        for dato in self._contacts:
            print(dato)

    def search_contacts(self):
        frase = input("Search contacts: ")
        try:
            for dato in self._contacts:
                if frase in dato["Name"] or frase in dato["Phone"]: 
                    datos = (dato["Name"] + " (" + dato["Phone"] + ")")
                    print(datos)
                else:
                    datos = None
            if datos is None:
                print("No contacts found")

            self.file.close()
        except ValueError:
            print("Valor incorrecto")
        self.file.close()
        
p = Phone()
p.search_contacts()
