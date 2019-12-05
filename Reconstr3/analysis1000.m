%%                      BEGINNING OF THE CODE
clear;
%%
Pts=readtable('text-1000','Delimiter',' ');
Pts=Pts{:,[1 3 2 31 17:25]};
MainPts=letplainonly(Pts);
%%
MainPts(:,14)=0*MainPts(:,5)+1*MainPts(:,6)+2*MainPts(:,7)+3*MainPts(:,8)+4*MainPts(:,9)+5*MainPts(:,10)+6*MainPts(:,11)+7*MainPts(:,12)+8*MainPts(:,13);
MainPts(:,5)=MainPts(:,14);
MainPts(:,6:14)=[];
MainPts(:,1:3)=double(int16((MainPts(:,1:3)./(2.^(-MainPts(:,5))*ones(1,3)))*2))/2;
MainPts(:,1:3)=MainPts(:,1:3).*(2.^(-MainPts(:,5))*ones(1,3));
%%
algorithm3;
%%
MainSurface=MainPts(index_final,:);
MainSurface2=MainPts(~index_final,:);
index=MainSurface(:,5)==level+1;
clear Y_Apply Z_Apply
save data-1000
%%
figure
plt(MainSurface(index,:),'.')
hold on
plt(MainSurface2,'.')
hold off
%%