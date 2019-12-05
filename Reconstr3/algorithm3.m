clc;
%%


%%                  PHASE 2
index_main=biggstS(Pts);
%%
index_final=false(size(MainPts,1),1);
%%
for level=0:7
    level
index=letlev(MainPts,level:level+1);
Pts=MainPts(index,:);
index1=letlev(Pts,level);
index2=letlev(Pts,level+1);
%%
index1(index1,:)=index_main;
%%
[s1, s2]=size(Pts);
%%
%%          Phase 1-2
Pts=sortrows(Pts,1);
Pts(:,s2+1)=transpose(1:s1);
XInterval=range(Pts,1);
%%          Phase 2-2
Pts=sortrows(Pts,2);
Pts(:,s2+2)=transpose(1:s1);
YInterval=range(Pts,2);
%%          Phase 3-2
Pts=sortrows(Pts,3);
Pts(:,s2+3)=transpose(1:s1);
ZInterval=range(Pts,3);
%%
Pts=sortrows(Pts,s2+3);
Pts=sortrows(Pts,s2+2);
Pts=sortrows(Pts,s2+1);
%%
Ids=Pts(:,end-2:end);
[X_Apply,Y_Apply,Z_Apply,Ref_Pts]=idlize_interval(XInterval,YInterval,ZInterval,Ids);
clear XInterval YInterval ZInterval
%%
Pts(:,end-2:end)=[];
Pts(1,6)=0;
%%
index_main=Alpha(X_Apply,Y_Apply,Z_Apply,Ref_Pts,index1,false(s1,1));
%%
index_final(index,:)=index_main;
index_main=index_main(index2,:);
clear s1 s2;
%%
end