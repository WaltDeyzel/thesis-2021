import Antenna.*
import selection.*

population_total = 100;
crossover_rate = 0.25;
mutation_rate = 0.05;
simulations = 100;

% Empty arry to host antennas.
population = Antenna.empty(population_total, 0);

% Antenna design. - linear array of 6.
% Half wave dipole antenna.
dp = dipole('Width',0.001, 'Length', 0.5);


% Fill population array
for i = 1:population_total
    % Randomize la
    la = linearArray;
    la.Element = [dp,dp,dp,dp,dp,dp];
    l1 = rand;
    l2 = rand;
    l3 = rand;
    la.ElementSpacing = [l1 l2 l3 l2 l1];
    %[l1 l2 l3 l2 l1]; % symetrical?
    %la.AmplitudeTaper = [rand rand rand rand rand rand];
    a = 360; % degrees
    la.PhaseShift = [round(rand*a) round(rand*a) round(rand*a) round(rand*a) round(rand*a) round(rand*a)];
    population(i) = Antenna(la, 3e8, 6, 1000);
end

fittest_antenna = population(1);
pop = zeros(simulations);
% Simulation - Gen 0
for a = 1:simulations
 
    disp("Generation " + string(a-1) )
    population_fitness = 0;
    for i = 1:population_total
        % calculate the fitness of each antenna.
        calc_fit = population(i).fitness();
        population_fitness = population_fitness + calc_fit;
        if calc_fit < fittest_antenna.Fitness
            fittest_antenna = Antenna(population(i).getArray(), 3e8, 6, calc_fit);
            disp('fittest : ' + string(fittest_antenna.Fitness))
            disp(fittest_antenna.antennaArray.ElementSpacing)
            %disp(fittest_antenna.antennaArray.PhaseShift)
        end
    end % end calculate fitness
    
    % Create copy of populaton.
    population_copy = Antenna.empty(population_total, 0);
    % Keep the best antenna. 
    population_copy(1) = fittest_antenna;
    disp('xxx : ' + string(population_copy(1).getFitness))
    for i = 2:(population_total)
        selected_1 = selection(population(:), population_total);
        
        if rand < crossover_rate
            % crossover
            selected_2 = selection(population(:), population_total);
            selected_1 = selected_1.crossover(selected_2);
        end
        
        if rand < mutation_rate
            % mutation
            selected_1.mutate()
        end
        
        population_copy(i) = Antenna(selected_1.getArray(), 3e8, 6, 1000);
    end
    population(:) = population_copy(:);
    disp('pop : ' + string(population_fitness/population_total))
    pop(a) = population_fitness;
   
end % end simulation

fittest_antenna.show;
disp(fittest_antenna.Fitness);
%plot(pop(:))
%title('Population error')
%xlabel('Error from fitness function') 
%ylabel('Generation (i)') 
%axis auto
