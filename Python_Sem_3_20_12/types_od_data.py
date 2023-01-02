my_list = [23, 423, 4523, 23, 235, 23]
my_tuple = tuple(my_list)
my_set = {234, 235, 2346, 346, 7654, 85}

my_dict = {
    4: 'rgg',
    6: 'rgg',
    'two': 'Dvoyka',
    (1,2,3): 'zdes kortezh',
    True: 'eto pravda'
}
my_dict[5] = 'eto pyatak'
my_dict[4] = 'eto chetyre'

# for i in my_dict:
    print(i)

for i in my_dict.items():
    print(i)


print(my_dict)

СРЕЗ:

print(list(range(-20, 40, 5))) # (ot, do(ne vkluchitelno), shag)
my_list = [23, 423, 4523, 23, 235, 23]
print(my_list[5])   - 23
print(my_list[1:5])  - [423, 4523, 23, 235]    
print(my_list[1:4:2])  - [423, 23]

[-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35]

[423, 4523, 23, 235]
[423, 23]