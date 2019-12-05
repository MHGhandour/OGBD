function RANGE=range(Pts,column)
RANGE=nan([size(Pts,1) 2]);
i=1;
while(isnan(RANGE(end,1)))
    j=find(Pts(:,column)==Pts(i,column) & Pts(:,5)==Pts(i,5),1,'last');
    I=find(Pts(:,column)>=Pts(i,column)-1.5*2^-Pts(1,5),1,'first');
    J=find(Pts(:,column)<=Pts(i,column)+1.5*2^-Pts(1,5),1,'last');
    RANGE(i:j,:)=[ones(j-i+1,1)*[I J]];
    i=j+1;
end
end
