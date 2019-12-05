%return index of all neighoursofasinglepoint
function [index,number_of_neighbours]=neighbours(pt,Pts)
level=pt(1,5);
%i=pt(1,5);
j=pt(1,2);k=pt(1,3);
%indexi=(Pts(:,5)==i+1 | Pts(:,5)==i-1 | Pts(:,5)==i);
indexj=(Pts(:,2)<=j+1.5*2^-level & Pts(:,2)>=j-1.5*2^-level);
indexk=(Pts(:,3)<=k+1.5*2^-level & Pts(:,3)>=k-1.5*2^-level);
index=indexj & indexk;% & indexi;
number_of_neighbours=sum(index);
end