transcription = input()
x_count = transcription.count('X')
o_count = transcription.count('O')

if x_count != o_count + 1 and x_count != o_count:
    print('?')
elif 'XX' in transcription:
    print('Alice')
elif 'OO' in transcription:
    print('Bob')
else:
    print('*')