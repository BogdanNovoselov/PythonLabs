import pandas as pd


def reduce(list, acc, fn):
    for el in list:
        acc = fn(el, acc)
    return acc


def map(list, fn):
    for i in range(len(list)):
        list[i] = fn(list[i])
    return list


# from handle init data
l = [1, 2, 3, 4, 5]
print(map(l, lambda x: x ** 2))


# from dataset
titanic = pd.read_csv('titanic.csv', header=0, delimiter=',')[:20]
titanic_people_survived = titanic[ (titanic.Survived == 1) & (titanic.Age > 0)]
average_age = reduce(titanic_people_survived['Age'], 0, lambda x, acc: x + acc) / len(titanic_people_survived['Age'])

print(average_age)