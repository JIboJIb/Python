# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
# passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is
# a valid email string.
import re

class Email:
    def __init__(self,email_title):
        self.email_title = email_title

    @ property
    def validate(self):
        regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.search(regex, self.email_title):
            return self.email_title
        else:
            return False

x = Email("hladkyi.vlados@gmail.com")
y = Email("qwff,m.il.com")

print(x.validate)
print(y.validate)