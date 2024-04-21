times = gets.split.map(&:to_i)
sh, sm, eh, em = times[0], times[1], times[2], times[3]

st = sh * 60 + sm
et = eh * 60 + em
d = et - st
if d <= 0
    d += 24 * 60
end
h = d / 60
m = d % 60
puts "O JOGO DUROU #{h} HORA(S) E #{m} MINUTO(S)"