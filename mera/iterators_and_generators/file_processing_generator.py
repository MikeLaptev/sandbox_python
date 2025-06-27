"""
Created on Aug, 11 2015

@author: mlaptev
"""


# Simple implementation
def file_processing(file_name="TCP_IP.txt", word_to_search="TCP"):
    string_number = 0
    with open(file_name, "r") as f:
        for line_in_file in f:
            string_number += 1
            if word_to_search in line_in_file:
                yield "{}: {}".format(
                    string_number,
                    (
                        line_in_file
                        if len(line_in_file) <= 68
                        else "{}{}".format(line_in_file[:68], "...")
                    ),
                )

            # Implementation with usage of Python's features


def file_processing_with_more_python_features(
    file_name="TCP_IP.txt", word_to_search="TCP"
):
    with open(file_name, "r") as f:
        for string_number, line_in_file in enumerate(f, 1):
            if word_to_search in line_in_file:
                yield "{}: {}".format(
                    string_number,
                    (
                        line_in_file
                        if len(line_in_file) <= 68
                        else "{}{}".format(line_in_file[:68], "...")
                    ),
                )


if __name__ == "__main__":
    # first solution
    print(">>> First Solution <<<")
    for line_info in file_processing():
        print(line_info)

    # second solution
    print()
    print(">>> Second Solution <<<")
    for line_info in file_processing_with_more_python_features():
        print(line_info)
