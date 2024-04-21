program Main;
var
    t, i, j, score1, score2: integer;
    correct, team1, team2: string;
    tieBreaker: boolean;
begin
    readln(t);
    for i := 1 to t do
    begin
        readln(correct);
        readln(team1);
        readln(team2);

        score1 := 0;
        score2 := 0;
        for j := 1 to length(correct) do
        begin
            if correct[j] = team1[j] then
                score1 := score1 + 1;
            if correct[j] = team2[j] then
                score2 := score2 + 1;
        end;

        writeln('Instancia ', i);
        if score1 > score2 then
            writeln('time 1')
        else if score1 < score2 then
            writeln('time 2')
        else
        begin
            tieBreaker := false;
            for j := 1 to length(correct) do
            begin
                if (correct[j] = team1[j]) and (correct[j] <> team2[j]) then
                begin
                    writeln('time 1');
                    tieBreaker := true;
                    break;
                end
                else if (correct[j] <> team1[j]) and (correct[j] = team2[j]) then
                begin
                    writeln('time 2');
                    tieBreaker := true;
                    break;
                end;
            end;
            if not tieBreaker then
                writeln('empate');
        end;
        writeln;
    end;
end.