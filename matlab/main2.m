import simulate.*
import saveGraph.*
            
population_total = 10;
crossover_rate = 0.5;
mutation_rate = 0.1;
simulations = 2;

path = "experiment/29Aug/";

angles = [30 60 45];
n = 1;
for steer = angles
    for i = 1:n
        % Name of excel file
        name = "sim"+string(steer)+"deg"+string(i)+".xlsx";
        % Dynamic path inside folder.
        path2 = path + string(steer)+"deg/";
        anss = simulate(population_total, crossover_rate, mutation_rate, simulations, (90-steer), path2+name);
        saveGraph(anss, steer, path2, i);  
    end
end

