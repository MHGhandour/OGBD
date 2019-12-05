function index_main=do(MainPts)


%%              PHASE 1
level=0;
index1=MainPts(:,5)==level;
Pts=MainPts(index1,1:5);
%%
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
%%
[XInterval,Y_Apply,Z_Apply,Ref_Pts]=idlize_interval(XInterval,YInterval,ZInterval,Ids);
clear YInterval ZInterval
%%
Pts(:,end-2:end)=[];
Pts(1,6)=0;
%%
clc
S=size(Ref_Pts,1);
index1=false(S,1);index1(1,1)=true;
%%
index_main=Alpha(XInterval,Y_Apply,Z_Apply,Ref_Pts,index1,false(S,1));