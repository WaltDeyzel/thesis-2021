% Progress plots

y1 = evol('M12:M999');
y2 = evol('N12:N999');
y3 = evol('O12:O999');
%y4 = evol('D12:D999');
%y5 = evol('E12:E999');
%y6 = evol('F12:F999');
%y7 = evol('G12:G999');
%y8 = evol('H12:H999');
%y9 = evol('I12:I999');
%y10 = evol('J12:J999');
%y11 = evol('K12:K999');

plot(y1,'LineWidth',1);
hold on
plot(y2,'LineWidth',1);
plot(y3,'LineWidth',1);
%plot(y4,'LineWidth',1);
%plot(y5,'LineWidth',1);
%plot(y6,'LineWidth',1);
%plot(y7,'LineWidth',1);
%plot(y8,'LineWidth',1);
%plot(y9,'LineWidth',2);
%plot(y10,'LineWidth',1);
%plot(y11,'LineWidth',1);

title('Error margin of the best solution per generation', 'FontSize',18)
xlabel('Generation','FontSize', 16) 
ylabel('Fitness Error','FontSize', 16) 
legend({'S_1','S_2', 'S_3'},'Location','southwest','FontSize', 14)
grid on



function amplitude = evol(xlRange1)
    filename = 'graphs/TEMP.xlsx';
    sheet = 2;
    amplitude = xlsread(filename,sheet,xlRange1); 
end