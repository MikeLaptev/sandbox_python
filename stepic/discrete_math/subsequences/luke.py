__author__ = 'mlaptev'


def generate_value_luke(till):
    prev_prev_value = 2.0
    prev_value = 1.0
    for i in range(till):
        if i == 0:
            yield prev_prev_value
        elif i == 1:
            yield prev_value
        else:
            yield prev_prev_value + prev_value
            prev_prev_value, prev_value = prev_value, prev_value + prev_prev_value


if __name__ == "__main__":
    # Simple launch
    for position, value in enumerate(generate_value_luke(51)):
        print(position, value)
