# Create your custom exception named `CustomException`, you can inherit from base Exception class, but extend its
# functionality to log every error message to a file named `logs.txt`. Tips: Use __init__ method to extend
# functionality for saving messages to file
# class CustomException(Exception):
# def __init__(self, msg):
class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open('logs.txt', 'w') as log:
            log.write(self.msg)


try:
    error = CustomException("Error")
except OSError:
    print("Check 'log.txt' file")
