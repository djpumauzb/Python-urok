def calc1(a, y):
    return a+y


def math(op, x, y):
    print(op(x, y))





math(lambda a,b: a + b, 5, 45)

# filter() function:

data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)

# zip ()

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]