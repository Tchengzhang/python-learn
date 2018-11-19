from concurrent.futures import ThreadPoolExecutor
import time


def printPerson(p):
    print(p)
    time.sleep(2)


person = ["tom", "lisa", "joe"]

# start1 = time.time()
# for p in person:
#     printPerson(p)
# end1 = time.time()
#
# print("time1: " + str(end1 - start1))

# start2 = time.time()
# with ThreadPoolExecutor(3) as executor:
#     for p in person:
#         executor.submit(printPerson, p)
# end2 = time.time()
# print("time2: " + str(end2 - start2))


start3 = time.time()
with ThreadPoolExecutor(3) as executor:
    executor.map(printPerson,person)
end3 = time.time()
print("time2: " + str(end3 - start3))
