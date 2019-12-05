function [List1,List2]=biggist_surface(List)
nList=List(:,8);
s=size(nList,1);j=0;k=0;
for i=2:s
    if(nList(i,1)>nList(i-1,1))
        j=j+1;
        A(j,1)=nList(i-1,1);
        A(j,2)=k;
        k=0;
    else
        k=k+1;
    end
end
A(j+1,:)=[nList(i,:) k];
%%
Maxx= A(:,2)==max(A(:,2));
%%
Max_id=A(Maxx,1);
%%
List1=List(:,8)==Max_id;

List2=List(~List1,:);
List1=List(List1,:);
end