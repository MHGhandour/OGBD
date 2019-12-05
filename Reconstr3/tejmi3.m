
%return droplets separated with indices
function List=tejmi3(Pts)
%i=1;
r=size(Pts,2); %for rows
m=0;
j=0;
S=size(Pts,1);
List=nan(S,r+1);
s=0;sp=-1;
while(s>sp && s<S)
sp=s;
m=m+1;s=s+1;
l=find(~isnan(Pts(:,1)),1,'first');
List(j+1,:)=[Pts(l,:) m];
Pts(l,:)=nan(1,r);
%Pts(1:l-1,:)=[];
%Pts(j+1,:)=nan(1,9);
while(j<s)
j=j+1;
Select=Pts(List(j,r-1):List(j,r),:);
[index,s2]=neighbours(List(j,:),Select);
List(s+1:s+s2,:)=[Select(index,:) m.*ones(s2,1)];
Select(index,:)=nan(s2,r);
Pts(List(j,r-1):List(j,r),:)=Select;
s=s+s2;
end
end
end