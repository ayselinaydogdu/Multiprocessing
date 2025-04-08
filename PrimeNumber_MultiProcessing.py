import multiprocessing
import time
import math

def PrimeOrNot(start, end, prime_number_list):
    for number in range(start, end+1):
        if number < 2:
            continue
        x = True
        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                x = False

        if x :
            prime_number_list.append(number)


def main():
    start = 0
    end = 100
    process_number = 4
    ranges = [(0, 25), (25, 50), (50, 75), (75, 100)]

    manager = multiprocessing.Manager()
    prime_number_list = manager.list()
    
    processes = []
    start = time.time()

    for start, end in ranges:
        p = multiprocessing.Process(target= PrimeOrNot, args= (start, end, prime_number_list))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    finish = time.time()
    total_time = finish - start

    print("Prime Numbers: ",  sorted(prime_number_list))
    print(f"Total Time: {total_time:.4f} seconds")

if __name__ == '__main__':
    main()