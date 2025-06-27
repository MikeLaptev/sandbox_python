# coding=utf-8
import requests

__author__ = "mlaptev"


def calculate_lines(input_url):
    r = requests.get(input_url)
    print((len(r.text.splitlines())))


if __name__ == "__main__":
    with open("dataset_3378_2.txt") as file_with_url:
        calculate_lines(file_with_url.read().strip())
