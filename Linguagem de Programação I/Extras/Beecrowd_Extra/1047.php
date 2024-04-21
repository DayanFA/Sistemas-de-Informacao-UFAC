<?php

$times = explode(" ", trim(fgets(STDIN)));
list($sh, $sm, $eh, $em) = array_map('intval', $times);

$st = $sh * 60 + $sm;
$et = $eh * 60 + $em;
$d = $et - $st;
if ($d <= 0) {
    $d += 24 * 60;
}
$h = intdiv($d, 60);
$m = $d % 60;
printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", $h, $m);

?>