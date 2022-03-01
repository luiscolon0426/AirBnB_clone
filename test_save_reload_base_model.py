#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("1")
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    print("2")
    obj = all_objs[obj_id]
    print(obj)
print("3")

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print("\n\n\n\n")
print("Hola")
print(storage.all())
print("Hola")
print("\n\n\n\n")
my_model.save()
