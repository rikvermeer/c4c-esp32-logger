#!/usr/bin/env python3

import addressbook_pb2
a = addressbook_pb2.AddressBook()
p = a.people.add()
#ph = p.phones.add()

person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME

phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME

print(person)
with open('empty_addressbook.dat', 'wb') as f:
    f.write(a.SerializeToString())

from google.protobuf import json_format as _json_format
print(_json_format.MessageToJson(person))
print(_json_format.MessageToJson(a))
print(_json_format.MessageToJson(p))
