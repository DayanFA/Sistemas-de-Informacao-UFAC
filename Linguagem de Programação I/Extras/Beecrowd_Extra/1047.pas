program GameDuration;
var
    sh, sm, eh, em, st, et, d, h, m: integer;
begin
    read(sh);
    read(sm);
    read(eh);
    read(em);
    st := sh * 60 + sm;
    et := eh * 60 + em;
    d := et - st;
    if d <= 0 then
        d := d + 24 * 60;
    h := d div 60;
    m := d mod 60;
    writeln('O JOGO DUROU ', h, ' HORA(S) E ', m, ' MINUTO(S)');
end.