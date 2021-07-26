# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own
# workers. You should implement a method that allows you to add workers to a Boss. You're not allowed to add
# instances of Boss class to workers list directly via access to attribute, use getters and setters instead!

class Person:
    def __init__(self, id_: int, name: str, company: str):
        self.id_ = id_
        self.name = name
        self.company = company


class Boss(Person):
    def __init__(self, id_, name, company, workers):
        super().__init__(id_, name, company)
        self.workers = []

    @property
    def list_workers(self):
        return self.workers

    @list_workers.setter
# перевіряємо, чи співпадає ім'я керівника у співробітника з керівником, до якого його додаємо
    def list_workers(self, worker):
        if worker.boss.name == self.name:
            # перевіряємо, чи співпадає компанія співробітника з компанією керівника, до якого його додаємо
            if worker.company == self.company:
                self.workers.append(worker)
            else:
                print(f"In company {self.company}  boss is {self.name}")
        else:
            print(f"{worker.name} works for {worker.boss.name}")


class Worker(Person):
    def __init__(self, id_, name, company, boss: Boss):
        super().__init__(id_, name, company)
        self.boss = boss


# створюємо керівників
my_boss_1 = Boss(1, 'Iryna', 'Biofarma', [])
my_boss_2 = Boss(2, 'Denys', 'Pharmak', [])

# створюємо співробітників
worker_1 = Worker(1, 'Victor', 'Biofarma', my_boss_1)
worker_2 = Worker(2, 'Olena', 'Biofarma', my_boss_1)
worker_3 = Worker(3, 'Oleksandr', 'Pharmak', my_boss_2)
worker_4 = Worker(4, 'Yulia', 'Pharmak', my_boss_2)

# додаємо співробітників першому керівнику
my_boss_1.list_workers = worker_1
my_boss_1.list_workers = worker_2

# додаємо співробітників другому керівнику
my_boss_2.list_workers = worker_3
my_boss_2.list_workers = worker_4

# додаємо співробітників керівникам, які не співпадають
my_boss_1.list_workers = worker_3
my_boss_2.list_workers = worker_1

# показуємо список співробітників для кожного керівника
print()
for worker in my_boss_1.list_workers:
    print(f'У {my_boss_1.name} працює {worker.name} (#{worker.id_}).')

print()
for worker in my_boss_2.list_workers:
    print(f'У {my_boss_2.name} працює {worker.name} (#{worker.id_}).')
