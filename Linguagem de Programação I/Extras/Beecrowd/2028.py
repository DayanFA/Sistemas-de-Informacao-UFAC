from sys import stdin

case = 1
for line in stdin:
    N = int(line)
    sequence = [str(i) for i in range(N+1) for _ in range(i)]
    sequence.insert(0, '0')  
    print(f'Caso {case}: {len(sequence)} numero{"s" if len(sequence) > 1 else ""}')
    print(' '.join(sequence))
    print()
    case += 1