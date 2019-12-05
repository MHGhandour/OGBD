clc
%%  Just temporary
Pts_initial=letlev(MainPts,[4 5]);
%Pts=MainPts;%(1:200000,:);
%%
Pts_initial=sortrows(Pts_initial,3);
Pts_initial=sortrows(Pts_initial,2);
Pts_initial=sortrows(Pts_initial,1);
Pts=letlev(Pts_initial,4);
 %%
Pts=Pts(:,1:5);
[s1, s2]=size(Pts);
%%          Phase 1
Pts=sortrows(Pts,1);
Pts(:,s2+1)=transpose(1:s1);
XInterval=range(Pts,1);
%%          Phase 2
Pts=sortrows(Pts,2);
Pts(:,s2+2)=transpose(1:s1);
YInterval=range(Pts,2);
%%          Phase 3
Pts=sortrows(Pts,3);
Pts(:,s2+3)=transpose(1:s1);
ZInterval=range(Pts,3);
%%
Pts=sortrows(Pts,s2+3);
Pts=sortrows(Pts,s2+2);
Pts=sortrows(Pts,s2+1);
%%
clear s1 s2;
%%
Ids=Pts(:,end-2:end);
%Ids(:,end+1:end+6)=[sortrows(Ids,2) sortrows(Ids,3)];
%%
%Ids=Ids(:,[1 4 7 ]);
%%
%Intervals=[XInterval YInterval ZInterval];
%clear Pts1 Pts2 Pts3
%%
%Ids=Ids(:,[1 4 7]);
[X_Apply,Y_Apply,Z_Apply,Ref_Pts]=idlize_interval(XInterval,YInterval,ZInterval,Ids);
clear XInterval YInterval ZInterval
%%
Pts(:,end-2:end)=[];
Pts(1,6)=0;
%%
Pts=Id_gathering(Pts,Ref_Pts,X_Apply,Y_Apply,Z_Apply);
%%






points1=Pts_initial(:,5)==4;
points2=Pts(:,6)==1;
%%
points1(points1,:)=points2;
%clc
%%  Just temporary
%Pts_initial=letlev(MainPts,[4 5]);
%Pts=MainPts;%(1:200000,:);

%Pts=letlev(Pts_initial,4);
%%
Pts=Pts_initial;
 %%
Pts=Pts(:,1:5);
[s1, s2]=size(Pts);
%%          Phase 1
Pts=sortrows(Pts,1);
Pts(:,s2+1)=transpose(1:s1);
XInterval=range(Pts,1);
%%          Phase 2
Pts=sortrows(Pts,2);
Pts(:,s2+2)=transpose(1:s1);
YInterval=range(Pts,2);
%%          Phase 3
Pts=sortrows(Pts,3);
Pts(:,s2+3)=transpose(1:s1);
ZInterval=range(Pts,3);
%%
Pts=sortrows(Pts,s2+3);
Pts=sortrows(Pts,s2+2);
Pts=sortrows(Pts,s2+1);
%%
clear s1 s2;
%%
Ids=Pts(:,end-2:end);
%Ids(:,end+1:end+6)=[sortrows(Ids,2) sortrows(Ids,3)];
%%
%Ids=Ids(:,[1 4 7 ]);
%%
%Intervals=[XInterval YInterval ZInterval];
%clear Pts1 Pts2 Pts3
%%
%Ids=Ids(:,[1 4 7]);
[X_Apply,Y_Apply,Z_Apply,Ref_Pts]=idlize_interval(XInterval,YInterval,ZInterval,Ids);
clear XInterval YInterval ZInterval
%%
Pts(:,end-2:end)=[];
Pts(1,6)=0;
%%
Pts=Id_gathering(Pts,Ref_Pts,X_Apply,Y_Apply,Z_Apply);
%%