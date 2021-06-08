# Create a function called make_country, which takes in a country’s name and capital as parameters. Then create
# a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. Make the function print out the values
# of the dictionary to make sure that it works as intended.
countries = {}


def make_country(name, capital):
    countries[name] = capital
    return countries


print(make_country("Ukraine", "Kiev"))
print(make_country("Spain", "Madrid"))
