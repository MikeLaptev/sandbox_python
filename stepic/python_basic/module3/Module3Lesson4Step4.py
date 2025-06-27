# coding=utf-8
__author__ = "mlaptev"


def process_students(input_file_name):
    math_statistic = list()
    physic_statistic = list()
    russian_statistic = list()
    with open(input_file_name) as input_file:
        for line in input_file:
            surname, math_mark, physic_mark, russian_mark = line.split(sep=";")
            print(((int(math_mark) + int(physic_mark) + int(russian_mark)) / 3))
            math_statistic.append(int(math_mark))
            physic_statistic.append(int(physic_mark))
            russian_statistic.append(int(russian_mark))
    print(
        (
            sum(math_statistic) / len(math_statistic),
            sum(physic_statistic) / len(physic_statistic),
            sum(russian_statistic) / len(russian_statistic),
        )
    )


if __name__ == "__main__":
    process_students("dataset_3363_4.txt")
