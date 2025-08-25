import datetime, random, threading, time


def runner():
    print('starting')
    time.sleep(random.randint(1, 3))
    print('waiting')
    event.wait()
    print(f'running at {datetime.datetime.now()}')


num_threads = 10
event = threading.Event()
threads = [threading.Thread(target=runner) for _ in range(num_threads)]
for t in threads:
    t.start()

event.set()
for t in threads:
    t.join()
