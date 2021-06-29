# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
# def stop_words(words: list):
#     pass
# @stop_words(['pepsi', 'BMW'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
def stop_words(words: list):
    def core(function):
        def wrap(*args):
            change_string = str(function(*args))
            for word in words:
                change_string = change_string.replace(word, "*")
            return change_string
        return wrap
    return core


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Vlad"))
