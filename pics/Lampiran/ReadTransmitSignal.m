% Read Signal

filename_transmit = 'path/to/file.bin';
data_type = 'float32';  % Adjust based on the file format 
fs = 28e6;              % Sampling frequency (Hz)
window_size = 2048;    % Size of FFT window
step_size = 1024;       % Step size for sliding window
observable = inf;

% Open and read binary file
file_transmit = fopen(filename_transmit, 'rb');
sentData = fread(file_transmit, observable, data_type);
fclose(file_transmit);

% Reconstruct complex numbers
real_part_transmit = sentData(1:2:end);
imag_part_transmit = sentData(2:2:end);
complex_data_transmit = complex(real_part_transmit, imag_part_transmit);
complex_data_transmit(1:28000000, :) = [];

% Time axis (if applicable)
n_samples_transmit = length(complex_data_transmit);
time_transmit = (0:n_samples_transmit-1) / fs;

% Compute instantaneous phase
inst_phase_transmit = unwrap(angle(complex_data_transmit));

% Compute instantaneous frequency
% Append 0 to match dimensions
inst_freq_chirp = [diff(inst_phase_transmit) * fs / (2 * pi); 0];  

% Plot the data
figure;

% Instantaneous frequency
plot(time_transmit, inst_freq_chirp);
title('Instantaneous Frequency of Chirp Transmitted');
xlabel('Time (s)');
ylabel('Frequency (Hz)');
grid on;