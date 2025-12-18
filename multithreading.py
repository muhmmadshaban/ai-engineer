import time
import threading
def square(values):
    print("Printing Squares")
    for i in values:
        time.sleep(0.2)
        print("Square : ",i*i)

def cube(values):
    print("Printing Cubes")
    for i in values:
        time.sleep(0.2)
        print("Cube : ",i*i*i)

arr=[2,3,4,5]
t=time.time()
# creates threads
t1=threading.Thread(target=square,args=(arr,))
t2=threading.Thread(target=cube,args=(arr,))

# start threads
t1.start()
t2.start()

# joining the threads
t1.join()
t2.join()
print("Total time ", time.time()-t)