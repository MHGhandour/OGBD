%%                      BEGINNING OF THE CODE
clear;
clc;
%%
MainPts=Organizer('text-10000');
%%
algorithm3;
%%
MainSurface=MainPts(index_final,:);
MainSurface2=MainPts(~index_final,:);
index=MainSurface(:,5)==level+1;
clear Y_Apply Z_Apply
save data-10000
%%
figure
plt(MainSurface(index,:),'.')
hold on
plt(MainSurface2,'.')
hold off
%%