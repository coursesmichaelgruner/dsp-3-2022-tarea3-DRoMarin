pkg load signal
M = str2num(argv(){1})
a = (1-str2num(argv(){2}))^M
z = zeros(1,M+1);
p = zeros(1,M+1);
p(1)=1;
p(M+1)=-a;
hold on
zplane(z,p)
pause
