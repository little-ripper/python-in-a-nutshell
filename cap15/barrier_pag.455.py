import datetime, random, threading, time


def runner():
    print('starting')
    time.sleep(random.randint(1, 3))
    print('waiting')
    try:
        my_number = barrier.wait()
    except threading.BrokenBarrierError:
        print('Barrier abort() or reset() called, thread exiting....')
        return
    print(f'running ({my_number}) at {datetime.datetime.now()}')


def announce_release():
    print('releasing')


num_threads = 10
barrier = threading.Barrier(num_threads, action=announce_release)

threads = [threading.Thread(target=runner) for _ in range(num_threads)]
for t in threads:
    t.start()

for t in threads:
    t.join()
