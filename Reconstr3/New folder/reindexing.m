function Pt=reindexing(Pt)
Pt=sortrows(Pt,4);
s=size(Pt,1);
i=1;
j=1;
Pt(1,5)=j;
i=i+1;
while (i<s+1)
    if(Pt(i,4)~=Pt(i-1,4))
    j=j+1;
    end
    Pt(i,5)=j;
    i=i+1;
end
Pt=[Pt(:,1:3) Pt(:,5)];
end