
%return droplets separated with indices
function List=tejmi3(Pts)
%i=1;
m=0;
j=0;
S=size(Pts,1);
List=nan(S,8);
s=0;sp=-1;
while(s>sp && s<S)
sp=s;
m=m+1;s=s+1;
l=find(~isnan(Pts(:,1)),1,'first');
List(j+1,:)=[Pts(l,:) m];
Pts(l,:)=nan(1,7);
%Pts(1:l-1,:)=[];
%Pts(j+1,:)=nan(1,9);
while(j<s)
j=j+1;
Select=Pts(List(j,6):List(j,7),:);
[index,s2]=neighbours(List(j,:),Select);
List(s+1:s+s2,:)=[Select(index,:) m.*ones(s2,1)];
Select(index,:)=nan(s2,7);
Pts(List(j,6):List(j,7),:)=Select;
s=s+s2;
end
end
end