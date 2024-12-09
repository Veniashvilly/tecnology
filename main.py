import threading
import time
import multiprocessing
import requests

# список url для АТ-01
urls = ['https://www.example.com'] * 10

def fetch_url(url):
    response = requests.get(url)
    return response.text

def sequence():
    print("Начинаем последовательное выполнение...")
    start_time = time.time()
    for url in urls:
        fetch_url(url)
    end_time = time.time()
    print(f"sequence time: {end_time - start_time:0.2f} секунд \n")

def threads():
    print("Начинаем выполнение с использованием потоков...")
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"threads time: {end_time - start_time:0.2f} секунд \n")

def processes():
    print("Начинаем выполнение с использованием процессов...")
    start_time = time.time()
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=fetch_url, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    end_time = time.time()
    print(f"processes time: {end_time - start_time:0.2f} секунд \n")

if __name__ == '__main__':
    #sequence()
    #threads()
    processes()


