function Pts=intervalise(Pts)
clear A B;
j=0;
s=size(Pts,1);
for i=2:s
    if(Pts(i,1)~=Pts(i-1,1) && Pts(i,5)==8)
    j=j+1;
    A(j)=i;  
    end
end
B=[1 1 A;A-ones(size(A)) s s];
A=[1 A;A-ones(size(A)) s];
B(2,:)=[B(2,2:end) NaN];
s2=size(A,2);
%%
for i=1:s2
    Pts(A(1,i):A(2,i),[6 7])=ones(-A(1,i)+A(2,i)+1,1)*[B(1,i) B(2,i)];
end  
end