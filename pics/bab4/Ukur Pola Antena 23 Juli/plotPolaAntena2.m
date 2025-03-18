close all;
clc;


% Take Antenna 1 Data From CSV 
A1data = readtable("Antena1.csv");
A1Degree = A1data{:,1};
A1Val = A1data{:,2};
A1Val = strrep(A1Val, ',', '.');
A1Val = str2double(A1Val);

% Take Antenna 2 Data From CSV
A2data = readtable("Antena2.csv");
A2Degree = A2data{:,1};
A2Val = A2data{:,2};
A2Val = strrep(A2Val, ',', '.');
A2Val =str2double(A2Val);

figure;
plot(A1Degree,A1Val);
xlabel('Derajat');
ylabel('S21 (dB)');
xticks = 0:5:360;
xlim([0,360]);
grid on;
set(gca,'GridColor','blue','GridLineStyle',':');
set(gca,'GridAlpha',0.7);
title("Antena 1 Log Periodic");

figure;
plot(A2Degree,A2Val);
xlabel('Derajat');
ylabel('S21 (dB)');
xlim([0,360]);
grid on;
set(gca,'GridColor','blue','GridLineStyle',':');
set(gca,'GridAlpha',0.7);
title("Antena 2 Log Periodic");



