% Laskari 3_3
close all
clear all

g=9.81
gamma=0.5
%m=0.020:0.005:0.060;
%m=0.020:0.01:0.060 *1000;
for askel=[5,10,20]
m=20:askel:60;


n=2;

v=(m*g/gamma).^(1/n);

sigmaM=1./m;
sigmaV=sigmaM*0+0.05;
logV=log(v);
logM=log(m);

D=sum(1./sigmaV.^2)*sum((logV./sigmaV).^2)-(sum(logV./sigmaV.^2))^2

sigmaN=1/D * sum(sigmaV.^2)

% sig=sigmaV;
% x=logV;
% D2= sum(1./sig.^2)*sum(x.^2./sig.^2)-(sum(x./sig.^2))^2

end


% D =
% 
%    3.9652e+05
% 
% 
% sigmaN =
% 
%    5.6744e-08
% 
% 
% D =
% 
%    1.5052e+05
% 
% 
% sigmaN =
% 
%    8.3046e-08
% 
% 
% D =
% 
%    7.4072e+04
% 
% 
% sigmaN =
% 
%    1.0125e-07
