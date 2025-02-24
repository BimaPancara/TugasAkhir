close all;
clc;

% Take Antenna 1 Data From CSV 
A1data = readtable("A1.csv");
A1Freq = A1data{:,1};
A1Val = A1data{:,2};
A1Freq = A1Freq/10^9;

% Take Antenna 2 Data From CSV
A2data = readtable("A2.csv");
A2Freq = A2data{:,1};
A2Val = A2data{:,2};
A2Freq = A2Freq/10^9;


figure;
plot(A1Freq,A1Val,'LineWidth',0.9,'Marker','.','Color',[0.9 0.1 0.3]);
xlabel('Frekuensi (GHz)');
ylabel('S11 (dB)');
grid on;
set(gca,'GridColor','blue','GridLineStyle',':');
set(gca,'GridAlpha',0.7);
title("Antena 1 Log Periodic");

figure;
plot(A2Freq,A2Val,'LineWidth',0.9,'Marker','.','Color',[0.3 0.1 0.9]);
xlabel('Frekuensi (GHz)');
ylabel('S11 (dB)');
ylim([-55,-10]);
grid on;
set(gca,'GridColor','blue','GridLineStyle',':');
set(gca,'GridAlpha',0.7);
title("Antena 2 Log Periodic");



