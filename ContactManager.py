import csv
import re

class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name}, Number: {self.number}, Email: {self.email}"

class ContactManager:
    def __init__(self, file_address="contacts.csv"):
        self.file_address = file_address
        try:
            file = open(self.file_address, 'r')
            lines = file.readlines()
            file.close()
            if(len(lines)==0):
                file = open(self.file_address, 'w')
                file.write("name,number,email\n")
                file.close()
        except:
            file = open(self.file_address, 'w')
            file.write("name,number,email\n")
            file.close()
        
        self.contacts = []
        self.read_contacts()
    
    def read_contacts(self):
        with open(self.file_address, 'r') as file:
            csvLines = csv.reader(file)
            next(csvLines)
            for line in csvLines:
                if len(line) == 3:
                    name, number, email = line
                    contact = Contact(name, number, email)
                    self.contacts.append(contact)

    def add_contact(self, name, number, email):
        if self.check_number(number) and self.check_email(email):
            contact = Contact(name, number, email)
            self.contacts.append(contact)
            self.save_file()
            print(f"{name} was added to the phone book!")
        else:
            print("Invalid input!")
    
    def edit_contact(self, name, new_name=None, new_number=None, new_email=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_name:
                    contact.name = new_name
                    print("Name changed!")
                if new_email:
                    if self.check_email(new_email):
                        contact.email = new_email
                        print("Email changed.")
                    else:
                        print("Invalid input for email!")
                if new_number:
                    if self.check_number(new_number):
                        contact.number = new_number
                        print("Number changed!")
                    else:
                        print("Invalid input for number!")
        self.save_file()
    
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
        self.save_file()
        print("Deleted!")
    
    def sort_contacts(self):
        self.contacts.sort(key=lambda contact: contact.name)
        self.save_file()
        print("Sorted!")
    
    def save_file(self):
        with open(self.file_address, 'w') as file:
            file.write("name,number,email\n")
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.number},{contact.email}\n")

    def check_number(self, number):
        regex = re.compile(r"^\+*\d{8,12}$")
        return bool(regex.match(number))
    
    def check_email(self, email):
        regex = re.compile(r"^.+\@.+\..+$")
        return bool(regex.match(email))
    
    def show_contacts(self):
        if not self.contacts:
            print("There is not any contacts.")
        else:
            for number, contact in enumerate(self.contacts):
                print(number+1, "-", contact)     

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    app = ContactManager()
    print("Hello! This is Contact Manager!")
    while True:
        print("--------------\nMenu:")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Show All Contacts")
        print("5. Sort Contacts")
        print("6. Exit")
        choice = input("Choose: ")

        if choice =='1':
            clear()
            name = input("Enter name: ")
            phone = input("Enter number: ")
            email = input("Enter email: ")
            clear()
            app.add_contact(name, phone, email)
        
        elif choice == '2':
            clear()
            name = input("Enter the name of the contact to edit: ")
            new_name = input("Enter new name (or leave empty): ")
            new_phone = input("Enter new phone (or leave empty): ")
            new_email = input("Enter new email (or leave empty): ")
            clear()
            app.edit_contact(name, new_name if new_name else None, new_phone if new_phone else None, new_email if new_email else None)
        
        elif choice == '3':
            clear()
            name = input("Enter the name of the contact to delete that: ")
            clear()
            app.delete_contact(name)
        
        elif choice == '4':
            clear()
            app.show_contacts()
        
        elif choice == '5':
            clear()
            app.sort_contacts()
        
        elif choice=='6':
            clear()
            print("Thanks for using this app.")
            break
        
        else:
            clear()
            print("Invalid input for menu. Please try again.")

if __name__ == "__main__":
    menu()
