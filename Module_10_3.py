import random
import threading
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            value = random.randint(50,500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            self.balance += value
            print(f'Пополнение: {value}. Баланс: {self.balance}')

    def take(self):
        for i in range(100):
            value = random.randint(50, 500)
            print(f'Запрос на {value}')
            if self.balance >= value:
                self.balance -= value
                print(f'Снятие: {value}, Баланс: {self.balance}')
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()


th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс {bk.balance}')


