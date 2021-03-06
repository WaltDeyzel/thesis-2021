
function y = optimizeSim(population_total, crossover_rate, mutation_rate, simulations, steer, path, space)
    import Antenna.*
    import selection.*
    import write2excel.*

    %TAKE FITTEST ANTENNA AND TRY TO MAKE IT EVEN BETTER BY TWEAKING ONLY ONE
    %PARAMETER AT A TIME.


    % Empty arry to host antennas.
    optimize_population = Antenna.empty(population_total, 0);
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
        la.ElementSpacing = space;
        a = 2;
        la.AmplitudeTaper = [1 1 1 1 1 1];
        a = 360; % degrees
        la.PhaseShift = [round(rand*a) round(rand*a) round(rand*a) round(rand*a) round(rand*a) round(rand*a)];
        optimize_population(i) = Antenna(la, 3e8, 6, 1000);
    end

    optimize_antenna = optimize_population(1);
    optimize_pop = zeros(simulations);
    % Simulation - Gen 0
    for a = 1:simulations

        disp("Generation " + string(a-1) )
        optimize_population_fitness = 0;
        for i = 1:population_total
            % calculate the fitness of each antenna.
            calc_fit = optimize_population(i).fitness(steer);
            optimize_population_fitness = optimize_population_fitness + calc_fit;
            if calc_fit < optimize_antenna.Fitness
                optimize_antenna = Antenna(optimize_population(i).getArray(), 3e8, 6, calc_fit);
            end
        end % end calculate fitness
         pop_norm = optimize_population_fitness/population_total;
        % Create copy of populaton.
        population_copy = Antenna.empty(population_total, 0);
        % Keep the best antenna. 
        population_copy(1) = optimize_antenna;
        write2excel(path, optimize_antenna, a, steer, pop_norm);
        if a == simulations
            y = optimize_antenna;
            break
        end
        %optimize_antenna.Azimuth
        disp('xxx : ' + string(population_copy(1).getFitness))

        for i = 2:(population_total)
            selected_1 = selection(optimize_population(:), population_total);

            if rand < crossover_rate
                % crossover
                selected_2 = selection(optimize_population(:), population_total);
                selected_1 = selected_1.crossover(selected_2);
            end

            if rand < mutation_rate
                % mutation
                if rand < 0.5
                    selected_1.mutatePhase()
                end
                if rand >= 0.5%selected_1.mutateSpacing()
                    selected_1.mutateAmp()
                end
            end

            population_copy(i) = Antenna(selected_1.getArray(), 3e8, 6, 1000);
        end
        optimize_population(:) = population_copy(:); 
    end % end simulation
end