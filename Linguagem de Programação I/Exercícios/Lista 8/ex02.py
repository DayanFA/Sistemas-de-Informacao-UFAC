d = [{'Fotos': 3, 'Likes': 21}, {'Comentários': 2, 'Compartilhamentos': 1},
     {'Fotos': 5, 'Likes': 33, 'Comentários': 8}, {'Fotos': 4, 'Compartilhamentos': 2},
     {'Fotos': 8, 'Comentários': 1}]

total_likes = 0

for post in d:
    try:
        total_likes += post['Likes']
    except KeyError:
        post['Likes'] = 0
        total_likes += post['Likes']

print(total_likes)
