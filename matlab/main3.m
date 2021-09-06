import optimizeSim.*
import saveGraph.*

population_total = 250;
crossover_rate = 0.5;
mutation_rate = 0.1;
simulations = 50;

path = "experiment/28Aug/";
path2 = path + "opz/";

angles = [30 45 60 80];
% solution for each steering degree.
spaces = [0.492 0.577 0.472 0.577 0.492; 
    0.434 0.5 0.501 0.5 0.434; 
    0.371 0.417 0.343 0.417 0.371; 
    0.114 0.504 0.44 0.504 0.114];

n = 3;
v = 1;
% When steer changes change spacing
for steer = angles
    space = spaces(v,:);
    disp(space)
    v = v + 1;
    path3 = path2 + string(steer)+"opz/";
    % sim n times for each angles
    for i = 1:n
        % optimize phase 
        file = "sim"+string(steer)+"opz"+string(i)+".xlsx";
        anss = optimizeSim(population_total, crossover_rate, mutation_rate, simulations, (90-steer), path3+file, space);
        saveGraph(anss, steer, path3, i);
        % amplitude
    end
end

