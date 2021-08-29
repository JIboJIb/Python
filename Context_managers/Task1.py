# File Context Manager class
# Create your own class, which can behave like a built-in function `open`.
# #Also, you need to extend its functionality with counter and logging.
# #Pay special attention to the implementation of `__exit__` method,
# which has to cover all the requirements to context managers mentioned here:
# https://docs.python.org/3.7/library/stdtypes.html#typecontextmanager
# https://docs.python.org/3.7/reference/compound_stmts.html#with


class Doc_ContextManager:
    counter = 0
    file_types = {
        'jpg': 0,
        'png': 0,
        'txt': 0,
        'other': 0
    }

    def __init__(self, first_name, last_name, type_file):
        self.first_name = first_name
        self.last_name = last_name
        self.type_file = type_file

    def open_dict(cls, type_file: str):
        for key in cls.file_types.keys():
            if key == type_file:
                value = cls.file_types.get(key)
                value += 1
                cls.file_types[key] = value
        return cls.file_types

    def __enter__(self):
        Doc_ContextManager.open_dict(self.type_file)
        Doc_ContextManager.counter += 1
        print(f'You write your name: {self.first_name} and surname: {self.last_name} {Doc_ContextManager.counter}.')
        return self

    def __exit__(self, exc_type, exc_tb, exc_value):
        print('Finishing work.')
        return None


class MyOpenFile_RP:
    file_counter = 0
    file_types_enabled = ['jpg', 'png', 'txt', 'py']
    file_types = {key: 0 for key in file_types_enabled}
    file_types['other'] = 0

    def __init__(self):
        pass

    def open_file(self, file, mode='r', add_str=None):
        file_ext = file.split('.')[-1]
        if file_ext in MyOpenFile_RP.file_types_enabled:
            if file_ext in MyOpenFile_RP.file_types.keys():
                MyOpenFile_RP.file_types.update({file_ext: MyOpenFile_RP.file_types[file_ext] + 1})
                print(MyOpenFile_RP.file_types)
        else:
            MyOpenFile_RP.file_types['other'] += 1
            raise TypeError('Тип файлу недоступний.')

        if mode == 'r':
            with open(file) as f:
                f.readlines()
        elif mode == 'w':
            with open(file, 'w') as f:
                f.write(add_str)
        elif mode == 'a':
            with open(file, 'a') as f:
                f.write(add_str)
        else:
            raise Exception('Вибраний Вами мод неіснує. Спробуйте використовувати тільки дані моди: "r", "w", "a".')
        return f


    @classmethod
    def get_num_of_usage(cls):
        return cls.file_counter

    @classmethod
    def get_num_of_usage_types(cls, type):
        for key in MyOpenFile_RP.file_types.keys():
            if type == key:
                value = MyOpenFile_RP.file_types[type]
                return value
        else:
            print('Даного типу неіснує.')


    def __enter__(self):
        MyOpenFile_RP.file_counter += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Закриття файлу. Кількість закриттів: {self.file_counter}.')
        return None
