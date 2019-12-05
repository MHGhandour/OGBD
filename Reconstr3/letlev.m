function index=letlev(MainPts,levels)
s=size(MainPts,1);
index=false(s,1);
for i=1:size(levels,2)
index=index | MainPts(:,5)==levels(i);
end
end
    

 
% function Pts=letlev(MainPts,levels)
% Pts=[];
% for i=1:size(levels,2)
% Pts=[Pts; MainPts(MainPts(:,5)==levels(i),:)];
% end
% end
