# Description: This file contains the Contact class, which is used to represent a contact in the phone book.
class Contact:
  def __init__(self, name, phone_number):
    self.name = name
    self.phone_number = phone_number
    
  def __str__(self):
    return f"Name: {self.name}, Phone: {self.phone_number}"
  
contact_example = Contact("Juan Pérez", "123456789")
print(contact_example)