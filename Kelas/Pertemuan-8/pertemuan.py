import json
import csv
# txt = text
# csv = coma separator value
# json = javascript object notation 


# file = open('data.txt', 'r')
# print(file)

# with open('data.txt', 'r') as file:
#     konten = file.read()
#     print(konten)

# with open('data.txt', 'a') as file:
#     file.write("\nDaffa,20,pria")

path = 'data.json'

def read_data():
    with open(path) as json_file:
        # return json_file
        return json.load(json_file)

def write_data(new_data):
    with open(path, 'w') as json_file:
        json.dump(new_data, json_file, indent=2)

data = read_data()

new_person = {
    "nama": "Adi",
    "umur": 16,
    "jenis_kelamin": "Pria"
}

data.append(new_person)

write_data(data)

print(data)


