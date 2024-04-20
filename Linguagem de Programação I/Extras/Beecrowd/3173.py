from datetime import datetime, timedelta

def solve():
    jupiter_period = 11.9 * 365.25
    saturn_period = 29.6 * 365.25
    initial_date = datetime(2020, 12, 21)
    N = int(input())
    jupiter_days = int(jupiter_period * N)
    saturn_days = int(saturn_period * N)
    jupiter_date = initial_date + timedelta(days=jupiter_days)
    saturn_date = initial_date + timedelta(days=saturn_days)
    print(f"Dias terrestres para Jupiter = {jupiter_days}")
    print(f"Data terrestre para Jupiter: {jupiter_date.strftime('%Y-%m-%d')}")
    print(f"Dias terrestres para Saturno = {saturn_days}")
    print(f"Data terrestre para Saturno: {saturn_date.strftime('%Y-%m-%d')}")

solve()