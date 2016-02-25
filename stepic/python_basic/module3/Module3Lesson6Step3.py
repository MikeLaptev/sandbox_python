# coding=utf-8
import requests
from urllib.parse import urljoin


__author__ = 'mlaptev'

base_url = "https://stepic.org/media/attachments/course67/3.6.3/"


def get_content_of_latest_file(file_url):
    """
    We are the champions, my friends,
    And we'll keep on fighting 'til the end.
    We are the champions.
    We are the champions.
    No time for losers
    'Cause we are the champions of the world.
    """
    r = requests.get(urljoin(base_url, file_url))
    index = 1
    while not r.text.startswith("We"):
        index += 1
        r = requests.get(urljoin(base_url, r.text))
    print(r.text)

if __name__ == "__main__":
    with open("dataset_3378_3.txt") as file_with_url:
        get_content_of_latest_file(file_with_url.read().strip())
