
function A=decompose(Pts_In,XInterval)
s=size(Pts_In,1);
m=Pts_In(1,1);
M=Pts_In(end,1); 
i=1;j=1;
A(j,1)=i; 
A(j,3)=XInterval(Pts_In(i,1),1);
A(j,4)=XInterval(Pts_In(i,1),2);
for i=2:s
    if (Pts_In(i,1)~=Pts_In(i-1,1))
        A(j,2)=i-1;
        j=j+1;
        A(j,1)=i;
        A(j,3)=XInterval(Pts_In(i,1),1);
        A(j,4)=XInterval(Pts_In(i,1),2);

    end
end
  A(end,2)=s; 

end