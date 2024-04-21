<?php
while (true) {
    $input = fgets(STDIN);
    if ($input === false) {
        break;
    }

    $inputs = explode(' ', trim($input));
    $L = intval($inputs[0]);
    $C = intval($inputs[1]);
    $R1 = intval($inputs[2]);
    $R2 = intval($inputs[3]);

    if ($L == 0 && $C == 0 && $R1 == 0 && $R2 == 0) {
        break;
    }

    if (max($R1, $R2) * 2 > min($L, $C)) {
        echo "N\n";
        continue;
    }

    if (pow($R1 + $R2, 2) <= pow($L - $R1 - $R2, 2) + pow($C - $R1 - $R2, 2)) {
        echo "S\n";
    } else {
        echo "N\n";
    }
}
?>