import sched, time

def enter_repeat(s, first_delay, period, priority, func, args):
    def repeating_wrapper():
        s.enter(period, priority, repeating_wrapper, ())
        func(*args)
    s.enter(first_delay, priority, repeating_wrapper, ())

s = sched.scheduler(time.monotonic, time.sleep)
enter_repeat(s, 1, 1, 1, print, ("Hello",))
s.run()
