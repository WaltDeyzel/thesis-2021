%fitfunc
function y = fitnessFunction(Adb_180)
    target = 90;
    fit = zeros(180,1);
    tot = 0;
    tally = 0;
    flag = 0;
    prev = Adb_180(1);
    for i = 1:180
        M = 10^(Adb_180(i)/20);
        fit(i) = M;
        if Adb_180(i) > prev
            prev = Adb_180(i);
            flag = 0;
        end
        if Adb_180(i) < prev && flag == 0 && i ~= target
            disp('w : ' + string(Adb_180(i)))
            tot = tot + M;
            tally = tally + 1;
            flag = 1;
            prev = Adb_180(i);
        end
        if flag == 1
            prev = Adb_180(i);
        end
    end
    y = -180*( (10^(Adb_180(target)/20)) - tot/tally ) / (sum(fit));
end