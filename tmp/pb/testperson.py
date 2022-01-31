#!/usr/bin/env python3

import addressbook_pb2
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
with open('person.dat', 'wb') as f:
    f.write(person.SerializeToString())
