%%                      BEGINNING OF THE CODE
        %%
clear;
load data6.mat   
clc;
%Pts2=[Pts(:,1) Pts(:,3) Pts(:,2)];
%%
Pts=letmaxlev(Pts);
%%
MainPts=letplainonly(Pts);
clear Pts;
%%
MainPts(:,14)=0*MainPts(:,5)+1*MainPts(:,6)+2*MainPts(:,7)+3*MainPts(:,8)+4*MainPts(:,9)+5*MainPts(:,10)+6*MainPts(:,11)+7*MainPts(:,12)+8*MainPts(:,13);
MainPts(:,5)=MainPts(:,14);
MainPts(:,6:14)=[];
%%
% remove gaps between actual gird listed andregular gird i want to see
MainPts(:,1:3)=double(int16((MainPts(:,1:3)./(2.^(-MainPts(:,5))*ones(1,3)))*2))/2;
MainPts(:,1:3)=MainPts(:,1:3).*(2.^(-MainPts(:,5))*ones(1,3));

%%                        New Algorithm

%%                      Sort then  make IDs

Pts=MainPts(1:20,:);
%%
Pts=Idlize(Pts);
%%
Pts=intervalise(Pts);
%%
List=tejmi3(Pts);
%pltgouttes(List);

%%                      Find the biggist surface


%[List1,List2]=biggist_surface(List);






