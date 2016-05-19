close all
clear all
%Laskari 1-3
d2Data=load('data.txt');
hold all
plot(d2Data(:,1),d2Data(:,2), '*')

% 2*V0 * exp(-(t/2T)^2)
% V0(1+cos(t/T))
T=1; %h
V0=1; %mV
%fplot(@(x) sin(x), [d2Data(1,1), d2Data(end,1)])
fplot(@(t) 2*V0*exp(-(t/(2*T))^2), [d2Data(1,1), d2Data(end,1)])
fplot(@(t) V0*(1+cos(t/T)), [d2Data(1,1), d2Data(end,1)])

hold off
