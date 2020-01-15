class ContactList(list):
    def __init__(self, contacts):
        self.contacts = contacts
    
    def search_by_name(self, name):
        self.name = name
        for i in self.contacts:
            if i == name:
                print(i)
            else:
                    pass

all_contacts = ContactList(["Will", "John", "Times", "Cates", "Smith"])
all_contacts.search_by_name("John")