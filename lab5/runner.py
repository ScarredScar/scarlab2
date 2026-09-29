import ctypes
import threading
import time

lib = ctypes.CDLL("./librace.so")

shared_counter = ctypes.c_int64.in_dll(lib, "shared_counter")
shared_counter.value = 0

print("Запуск двух потоков с ассемблерным кодом (с LOCK)...")
start_time = time.time()

t1 = threading.Thread(target=lib.thread_function)
t2 = threading.Thread(target=lib.thread_function)

t1.start()
t2.start()
t1.join()
t2.join()

expected = 20000000
actual = shared_counter.value

print(f"Время выполнения: {time.time() - start_time:.4f} сек.")
print(f"Ожидаемый результат: {expected}")
print(f"Фактический результат: {actual}")
print(f"Потеряно инкрементов: {expected - actual}")
