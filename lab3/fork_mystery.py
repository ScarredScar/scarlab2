import os
import time

shared_counter = 42

print(f"[РОДИТЕЛЬ] Начальный процесс. PID: {os.getpid()}, Адрес counter: {hex(id(shared_counter))}")
print("Выполняем системный вызов fork()...\n")

pid = os.fork()

if pid == 0:
    print(f"[ПОТОМК] Я родился! Мой PID: {os.getpid()}, PID родителя: {os.getppid()}")
    print(f"[ПОТОМК] Значение counter до изменения: {shared_counter}, Адрес: {hex(id(shared_counter))}")
    shared_counter = 999
    print(f"[ПОТОМК] Изменил counter! Новое значение: {shared_counter}, Новый адрес: {hex(id(shared_counter))}")
else:
    time.sleep(1)
    print(f"[РОДИТЕЛЬ] Проверяю переменную после паузы...")
    print(f"[РОДИТЕЛЬ] Значение counter: {shared_counter}, Адрес: {hex(id(shared_counter))}")
