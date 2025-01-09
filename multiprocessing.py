import os
import time
from multiprocessing import Pool

os.system('COLOR B')


def read_info(file_path):
    all_data = []

    with open(file_path, mode='r') as file:
        for line in file:
            if line.strip():
                all_data.append(line.strip())

    return all_data


if __name__ == "__main__":
    # Указываем путь к папке с файлами
    directory = "./files"
    filenames = [os.path.join(directory, f"file_{num}.txt" for num in range(1, 5))]

    start = time.time()
    results = []

    for filename in filenames:
        results.extend(read_info(filename))

    end = time.time()
    linear_time = end - start

    print(f"Время выполнения линейного подхода: {linear_time:.7f}")

    start = time.time()

    with Pool(processes=len(filenames)) as pool:
        results = pool.map(read_info, filenames)

    end = time.time()
    parallel_time = end - start

    print(f"Время выполнения многопроцессорного подхода: {parallel_time:.7f}")
    print(f"Линейный подход занял {linear_time:.7f} сек., многопроцессорный подход занял {parallel_time:.7f} сек.")

    if linear_time > parallel_time:
        print("Многопроцессорный подход быстрее!")
    elif linear_time < parallel_time:
        print("Линейный подход оказался быстрее.")

    print("Результаты чтения:")

    for filename, data in zip(filenames, results):
        print(f"Файл {filename}: первые 5 строк")
        print("\n".join(data[:5]))
        print()

    print("Окончательный результаты: ", results)

try:
    os.system('PAUSE')
except:
    os.system('CLS')
