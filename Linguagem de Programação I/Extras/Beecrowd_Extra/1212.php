<?php

while (true) {
    $input = explode(" ", trim(fgets(STDIN)));
    $a = strval($input[0]);
    $b = strval($input[1]);
    $carry = 0;
    $c = 0;
    if ($a == '0' && $b == '0') {
        break;
    }

    while (strlen($a) < strlen($b)) {
        $a = '0' . $a;
    }
    while (strlen($b) < strlen($a)) {
        $b = '0' . $b;
    }

    for ($i = strlen($a) - 1; $i >= 0; $i--) {
        if ((intval($a[$i]) + intval($b[$i]) > 9) || (intval($a[$i]) + intval($b[$i]) + $c > 9)) {
            $carry += 1;
            $c = 1;
        } else {
            $c = 0;
        }
    }

    if ($carry == 0) {
        echo "No carry operation.\n";
    } elseif ($carry == 1) {
        echo "1 carry operation.\n";
    } else {
        echo "$carry carry operations.\n";
    }
}

?>