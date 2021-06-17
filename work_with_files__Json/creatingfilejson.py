# Extend Phonebook application
# Functionality of Phonebook application:
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
#
# The first argument to the application should be the name of the phonebook. Application should load JSON data, if it
# is present in the folder with application, else raise an error. After the user exits, all data should be saved
# to loaded JSON.
import json
phonebook = {
  "0932082802": {
    "name": "Vladyslav",
    "last_name": "Hladkyi",
    "city": "Kiev"
  },
  "0932082801": {
    "name": "Daria",
    "last_name": "Hladka",
    "city": "Lutsk"
  }
}
with open("phonebook.json", "w") as phonelist:
    # open(name of the file, mode of interaction) as name for python     create a file JSON
    json.dump(phonebook, phonelist, indent=2)
#  json.dump(object which you want to save, python name where will be save the data)  save the vocabulary in JSON
