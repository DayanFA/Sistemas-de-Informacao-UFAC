marmores = []
T = 1
while true
    N, Q = gets.split.map(&:to_i)
    break if N == 0 && Q == 0

    marmores = Array.new(N)
    for i in 0...N
        marmores[i] = gets.to_i
    end

    marmores.sort!

    puts "CASE# #{T}:"
    T += 1
    for _ in 0...Q
        consulta = gets.to_i

        index = marmores.bsearch_index { |x| x >= consulta }

        if index.nil? || marmores[index] != consulta
            puts "#{consulta} not found"
        else
            puts "#{consulta} found at #{index + 1}"
        end
    end
end