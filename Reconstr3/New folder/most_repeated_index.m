% find the most index repeated in the list
function id=most_repeated_index(Points)
mi=min(Points(:,4));
ma=max(Points(:,4));
A=zeros(1,(ma-mi));
for i=mi:ma
    a=find(Points(:,4)==i);
    A(i)=size(a,1);
       
end
id=find(A==max(A));
end