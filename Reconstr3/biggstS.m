function index = biggstS(Pts)
M=max(Pts(:,6));
for i=1:M
    index=Pts(:,6)==i;
    A(i)=sum(index);
end
i=find(A==max(A));
index=Pts(:,6)==i;
end