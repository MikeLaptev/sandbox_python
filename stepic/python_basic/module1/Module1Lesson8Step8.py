__author__ = "mlaptev"

if __name__ == "__main__":
    time_to_sleep = int(eval(input()))
    current_hours = int(eval(input()))
    current_minutes = int(eval(input()))
    alarm_minutes = time_to_sleep + current_hours * 60 + current_minutes
    print(((alarm_minutes // 60) % 24))
    print((alarm_minutes % 60))
