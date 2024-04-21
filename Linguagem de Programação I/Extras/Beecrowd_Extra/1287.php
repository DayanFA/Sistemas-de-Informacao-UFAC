<?php
while (true) {
    $s = fgets(STDIN);
    if ($s === false) {
        break;
    }

    $s = str_replace(['O', 'o', 'l', ',', ' '], ['0', '0', '1', '', ''], trim($s));

    if (!ctype_digit($s) || intval($s) > 2147483647) {
        echo "error\n";
    } else {
        echo intval($s) . "\n";
    }
}
?>