__author__ = 'mlaptev'

if __name__ == "__main__":
    time_to_sleep = int(input())
    current_hours = int(input())
    current_minutes = int(input())
    alarm_minutes = time_to_sleep + current_hours*60 + current_minutes
    print((alarm_minutes//60) % 24)
    print(alarm_minutes % 60)
