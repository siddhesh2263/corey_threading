import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds_list = [5, 4, 3, 2, 1]
    # List comprehension
    results = [executor.submit(do_something, sec) for sec in seconds_list]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')