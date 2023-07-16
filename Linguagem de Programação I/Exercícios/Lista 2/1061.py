from datetime import timedelta
inicio_dia = input().split(' ')
inicio_time = input().split(':')
day1 = int(inicio_dia[1])
hora_inicio = int(inicio_time[0])
min_inicio = int(inicio_time[1])
seg_inicio = int(inicio_time[2])
final_dia = input().split(' ')
final_time = input().split(':')
day2 = int(final_dia[1])
hora_final = int(final_time[0])
min_final = int(final_time[1])
seg_final = int(final_time[2])
t1 = timedelta(days=day1, hours=hora_inicio, minutes=min_inicio, seconds=seg_inicio)
t2 = timedelta(days=day2, hours=hora_final, minutes=min_final, seconds=seg_final)
t3 = t2 - t1
hours = t3.seconds // 3600
seconds = t3.seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print("%d dia(s)" % t3.days)
print("%d hora(s)" % hours)
print("%d minuto(s)" % minutes)
print("%d segundo(s)" % seconds)
