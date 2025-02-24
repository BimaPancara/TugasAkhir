% Drop Data if necessary
% Calculate the difference in lengths
difference = length(complex_data_transmit) - length(complex_data);

% Trim the extra elements from the end of complex_data
complex_data_transmit_trimmed = complex_data_transmit(1:end-difference);

% Ranging
% StrecProc = dechirp(Rx, Tx)
StrecProc = complex_data_transmit_trimmed .* conj(complex_data);

% Plot the spectrum before dechirping. 
[Pxx,F] = periodogram(complex_data,[],1024,fs,'centered');
plot(F/1000,10*log10(Pxx)); grid;
xlabel('Frequency (kHz)');
ylabel('Power/Frequency (dB/Hz)');
title('Periodogram Power Spectral Density Estimate Before Dechirping');

% Plot the spectrum after dechirping.
[Pyy,F] = periodogram(StrecProc,[],1024,fs,'centered');
plot(F/1000,10*log10(Pyy));
xlabel('Frequency (kHz)');
ylabel('Power/Frequency (dB/Hz)');
ylim([-100 -30]); grid
title('Periodogram Power Spectral Density Estimate After Dechirping 6 Meter');