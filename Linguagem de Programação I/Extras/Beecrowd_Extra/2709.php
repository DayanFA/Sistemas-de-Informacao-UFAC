<?php
function isPrime($n) {
    if ($n < 2) return false;
    if ($n == 2) return true;
    if ($n % 2 == 0) return false;
    for ($p = 3; $p * $p <= $n; $p += 2) {
        if ($n % $p == 0) return false;
    }
    return true;
}

while (true) {
    $M = intval(fgets(STDIN));
    if ($M === 0) break;
    $coins = [];
    for ($i = 0; $i < $M; $i++) {
        $coins[] = intval(fgets(STDIN));
    }
    $N = intval(fgets(STDIN));
    $sumCoins = 0;
    for ($i = $M - 1; $i >= 0; $i -= $N) {
        $sumCoins += $coins[$i];
    }
    if (isPrime($sumCoins)) {
        echo "You’re a coastal aircraft, Robbie, a large silver aircraft.\n";
    } else {
        echo "Bad boy! I’ll hit you.\n";
    }
}
?>