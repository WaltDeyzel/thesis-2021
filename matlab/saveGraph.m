
function saveGraph(LAA, steer, path, no) %Linear antenna array
    import uniformLinearArray.*
    import grpahNormdB.*
    
    Adb_GA = patternAzimuth(LAA.antennaArray, 3e8, 0, 'Azimuth',0:1:180);
    Adb_un = patternAzimuth(uniformLinearArray(0.5, steer), 3e8, 0, 'Azimuth',0:1:180);
    
    gcf = figure ;
    set(gcf, 'Visible', 'off');
    %set(gcf,'position',get(0,'ScreenSize'))
    hold on

    plot((Adb_un - max(Adb_un)),'LineWidth',1)
    plot((Adb_GA - max(Adb_GA)),'LineWidth',1)

    title('Beam steered ' + string(steer) + '^{\circ}','FontSize', 18)
    xlabel('Degrees','FontSize', 16) 
    ylabel('Amplitude Normalized (dB)','FontSize', 16) 
    legend({'Uniform','non-uniform'},'FontSize', 14)
    grid on
    saveas(gcf, path + 'plot' + string(steer)+'deg_'+string(no)'+'.jpg')
    saveas(gcf, path + 'plot' + string(steer)+'deg_'+string(no)'+'.emf')
    
    
    gcf = figure;
    hold on
    set(gcf, 'Visible', 'off');
    patternAzimuth(LAA.antennaArray, 3e8, 0, 'Azimuth',0:1:180);
    warning('off')
    saveas(gcf,path +'pol' + string(steer)+'deg_'+string(no)'+'.jpg')
    saveas(gcf,path +'pol' + string(steer)+'deg_'+string(no)'+'.emf')
    
    close all
end