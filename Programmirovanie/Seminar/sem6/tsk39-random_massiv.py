import random


def random_array(length: int, minnimum: int, maximum: int) -> list:
    new_list = []
    for a in range(length):
        new_list.append(random.randint(minnimum, maximum))
    return new_list


def input_array():
    length = int(input("Введите количество элементов: "))
    start = int(input("Введите минимальный диапазон: "))
    end = int(input("Введите максимальный диапазон: "))
    print(random_array(length, start, end))


def main():
    input_array()


if __name__ == "__main__":
    main()
