import threading


def job_1():
    lock.acquire()
    print('First thread started')


def job_2():
    lock.acquire()
    print('Second thread started')


t = threading.Thread(target=job_1)
tt = threading.Thread(target=job_2)
lock = threading.Lock()
t.start()
tt.start()
