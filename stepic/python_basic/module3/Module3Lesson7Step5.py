# coding=utf-8
__author__ = 'mlaptev'


if __name__ == "__main__":
    school = dict()
    for i in range(1, 12):
        school[i] = list()
    with open("dataset_3380_5.txt") as input_file:
        for line in input_file:
            class_id, surname, height = line.split(sep='\t')
            school[int(class_id)].append(int(height))
    for class_id, height_statistic in school.items():
        if len(height_statistic) == 0:
            print("{} -".format(class_id))
        else:
            print("{} {}".format(class_id, sum(height_statistic)/len(height_statistic)))
