% Laskari 3_3
close all
clear all

g=9.81
gamma=0.5
%m=0.020:0.005:0.060;
%m=0.020:0.01:0.060 *1000;
m=20:5:60;


n=2

v=(m*g/gamma).^(1/n);

sigmaM=1./m
sigmaV=sigmaM*0+0.05
logV=log(v);
logM=log(m);

%errorbarxy(log(v),log(m),sigmaM,sigmaV)
errorbarxy(logV,logM,sigmaV,sigmaM)
% Create xlabel
xlabel('log(Nopeus) [m/s]','FontWeight','bold','FontSize',16);

% Create ylabel
ylabel('log(Massa) [A.U.]','FontWeight','bold','FontSize',16);

% Create title
title({'Skaalamaton logaritminen massan plottaus nopeuden funktiona'},...
    'FontSize',20);

%% Suorien sovitus

x1=3.485
y1=4.093

x0=3.036
y0=3.001

x=2.95:0.1:3.55;
y=(y1-y0)*(x-x0)/(x1-x0)+y0;
hold all;
plot(x,y)
hold off

%% ja toinen suora
x1=3.54
y1=4.117

x0=2.981
y0=2.941

x=2.95:0.1:3.55;
y=(y1-y0)*(x-x0)/(x1-x0)+y0;
hold all;
plot(x,y)
hold off
