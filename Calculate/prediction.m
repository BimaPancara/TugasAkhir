% Hitung jarak dengan
% d0 = (c Tc fb)/(2 B)

syms fb d

eqn = d == (3*10^8*0.001667*fb)/(2*50);

c = 3*10^8;     % m/s
Tc = 0.001667;  % s
B = 50;         % Mhz



for d=1:3:18
    fbSolv(fb,1) = solve(eqn,fb);
end

%for d0=0:3:18
 %   fbSolv = solve(eqn,fb);
%end


