A, B, C = map(int, input().split())

if B < A and C >= B:
    print(":)")
elif B > A and C <= B:
    print(":(")
elif B > A and C > B and C - B < B - A:
    print(":(")
elif B > A and C > B and C - B >= B - A:
    print(":)")
elif B < A and C < B and B - C < A - B:
    print(":)")
elif B < A and C < B and B - C >= A - B:
    print(":(")
elif B == A and C > B:
    print(":)")
elif B == A and C <= B:
    print(":(")