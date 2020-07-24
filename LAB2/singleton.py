class SingletonPattern:
    def __init__(self, some_class):
        self.some_class = some_class
        self.example_obj = None

    def __call__(self, *args, **kwargs):
        if self.example_obj is None:
            self.example_obj = self.some_class(*args, **kwargs)
        return self.example_obj

@SingletonPattern
class Worker:
    def __init__(self, name, surname, year, pay):
        self.name = name
        self.surname = surname
        self.year = year
        self.pay = pay

    def __str__(self):
        return self.name + " " + self.surname + " age: " + str(self.year) + " pay: " + str(self.pay)

if __name__ == "__main__":
    worker1=Worker("Tom", "Johnson", 26, 5000)
    worker2=Worker("Bob", "Robinson", 30, 6500)

    print(worker1, worker2)
    print(worker1 == worker2)