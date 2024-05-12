<?php

class Pair {
    public $key;
    public $value;

    public function __construct($key, $value) {
        $this->key = $key;
        $this->value = $value;
    }
}

function compare($a, $b) {
    return $a->key - $b->key;
}

$T = 0;
while (($N = intval(fgets(STDIN))) != 0) {
    if ($T > 0) {
        echo "\n";
    }

    $totalX = 0;
    $totalY = 0;
    $consumos = [];
    for ($i = 0; $i < $N; $i++) {
        list($X, $Y) = array_map('intval', explode(' ', fgets(STDIN)));
        $totalX += $X;
        $totalY += $Y;
        $key = intval($Y / $X);
        $found = false;
        foreach ($consumos as $pair) {
            if ($pair->key == $key) {
                $pair->value += $X;
                $found = true;
                break;
            }
        }
        if (!$found) {
            $consumos[] = new Pair($key, $X);
        }
    }

    $T += 1;
    echo "Cidade# $T:\n";

    usort($consumos, 'compare');
    foreach ($consumos as $pair) {
        echo "$pair->value-$pair->key ";
    }
    echo "\n";

    $consumo_medio = floor((100.0 * $totalY) / $totalX) / 100;
    echo "Consumo medio: " . number_format($consumo_medio, 2) . " m3.\n";
}

?>