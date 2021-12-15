import time
a = time.time()
print("seconds:",a)
print("\n")

print("current date and time:")
print(time.ctime(a))

time.sleep(1)
print("\nexecution starts after a second")

print("localtime")
print(time.localtime(a))

c = time.localtime()
d = time.strftime("%m,%d,%Y,%H,%M,%S",c)
print(d)
e ="12 NOVEMBER, 2021"
f=time.strptime(e,"%d %B, %Y")
print(f)
