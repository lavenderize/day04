# about tuple

a = 'harry',        #tuple
b = ('harry',)
c = ()              # empty tuple
d = 'harry', 'ron'
e = ('Hermione')    # string type
f = ('harry', 'ron')

# tuple exchange

password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password     # position exchange

# list to tuple

marx_list = ['Groucho', 'Chico', 'Harpo']
tuple(marx_list)

# modify a tuple

tuple_a = ('Fee', 'Fie', 'Foe')
tuple_b = ('Flop',)
t = tuple_a + tuple_b

tuple_a = tuple_a + tuple_b     # overwrite

# about list

scores = ('B+', 'A+', 'C+')

temp = list(scores)
temp[1] = 'C+'
temp[2] = 'A+'
scores = tuple(temp)
# print(scores[1], scores[2])

# append, insert

alpha_list = ['a', 'b', 'c']
alpha_list.append('z')      # 맨 뒤에 삽입
alpha_list.insert(1, 'i')   # 특정 위치에 삽입

beta_list = ['w', 'y', 'x']
beta_list = beta_list + alpha_list
# beta_list.append(alpha_list)

# print(alpha_list)
# print(beta_list[0])

# list에서 항목 삭제하기 - pop
# sort(), sorted()

primes = [2, 19, 3.0, 5, 7, 11]
primes.sort()   # 원본 자체의 순서를 규칙대로 정렬
# print(primes)

# primes_sorted = sorted(primes) # 정렬된 리스트를 새롭게 생성
# print(primes_sorted)

# shallow copy
# deep copy

# list comprehension

# odd_lists = []
# for i in range(1, 11):
#    if i % 2 == 1:
#        odd_lists.append(i)

odd_lists = [i for i in range(1, 11) if i % 2 == 1]
print(odd_lists)


# about dictionary

students = {'name': 'Kim Inha', 'age' : 23, 'eyes': [0.9, 1.1]}
# for k in students.keys():
#     print(k)

# for k in students.values():
#    print(k)

for k, v in students.items():
    print(f'{k} : {v}')

print(f'이름은 {students["name"]}, 나이는 {students["age"]}세,', end=' ')
print(f'시력은 좌: {students["eyes"][0]}, 우: {students["eyes"][1]}')