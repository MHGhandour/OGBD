%return index of all neighoursofasinglepoint
function [index,number_of_neighbours]=neighbours(pt,Pts)
%i=pt(1,5);
j=pt(1,2);k=pt(1,3);
%indexi=(Pts(:,5)==i+1 | Pts(:,5)==i-1 | Pts(:,5)==i);
indexj=(Pts(:,2)<=j+2^-8 & Pts(:,2)>=j-2^-8);
indexk=(Pts(:,3)<=k+2^-8 & Pts(:,3)>=k-2^-8);
index=indexj & indexk;% & indexi;
number_of_neighbours=sum(index);
end