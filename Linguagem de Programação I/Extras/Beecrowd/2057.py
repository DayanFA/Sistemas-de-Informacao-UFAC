def calculate_arrival_time():
    S, T, F = map(int, input().split())
    arrival_time = (S + T + F) % 24
    print(arrival_time)

calculate_arrival_time()