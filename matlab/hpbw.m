
function y = hpbw(LAA)
    Adb_GA = patternAzimuth(LAA, 3e8, 0, 'Azimuth',0:1:180);
    
    peak_1 = -90;
    peak_2 = -100;
    target = 0.0;
    target_2 = 0.0;
    for i = 1:180
        dbm = Adb_GA(i); % in decibals
        % determine if current i is a peak
        if ((i > 1 && i < 180) && (Adb_GA(i-1) < dbm) && (Adb_GA(i+1) < dbm))
           % second largest peak
            if dbm > peak_2 && dbm < peak_1
                peak_2 = dbm;
                target_2 = i;
            end
            if dbm > peak_1
                peak_1 = dbm;
                target = i;
            end
        end
    end
    hp = 0;
    for i = 1:target-1
        hp = hp + 1;
        if Adb_GA(target-i) <= peak_1 - 3
            break
        end
    end
    
    for i = 1:(180-target-1)
        hp = hp + 1;
        if Adb_GA(target+i) <= peak_1 - 3
            break
        end
    end
    patternAzimuth(LAA, 3e8, 0, 'Azimuth',0:1:180);
    y = [hp, peak_1, target, peak_2, target_2];
   
    
end