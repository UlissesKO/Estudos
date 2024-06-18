for x in range(10):
    print(x)


bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}

for bear in bears:
    if bears[bear] == 'friendly':
        print("Hello, "+bear+" bear!")
    else:
        print('odd')


age = {"Jim": 31,'Nick': 43,'John': 54, 'Seth': 65}
print(age.keys())

for name in age:
    print(name, age[name])

for name in sorted(age):
    print(name, age[name])

for name in sorted(age, reverse= True):
    print(name, age[name])


n=100
number_of_times = 0
while n >= 1:
    n //= 2
    number_of_times += 1
print(number_of_times)