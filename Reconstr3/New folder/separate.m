function group=separate(Pts,dist)
% Pts: non organized list.
% dist: cell size - distance between cells
% group :separate group of points representing a droplet (or a single
% continued surface)
group=nan(size(Pts));%initial allocating
s=1;%represents the size of not nan in "group" variable actually is 
    %(will be same as Pts at the end, and will be used to add to element at
    % each while loop considering the neighbours of each cell already found
    % (loop inside the loop)
j=0;%will be an index going into the loop inside the loop regarding the 
    %cell we want to examine to find all his neighbour
m=1;%design the number of groups we find (will increase each time we
    %finish gathering neighbours in a group (at the end of the first loop)
l=1;%Design the first not nan number in Pts, will be [] at the final lap 
    %of the first loop
while(size(l,1)>0) 
    group(s,:)=[Pts(1,1:3) m];%first element of a droplet
    Pts(1,:)=[NaN NaN NaN NaN];%remove him from the non organized list
    while (j<s)
        
        
        j=j+1;%increasing j to test all element already found for any 
              %neighbour around
        i=all_direction(group(j,:),Pts,dist);
        s2=size(i,1);
        group(s+1:s+s2,:)= [Pts(i,1:3) m.*ones(s2,1)];
        Pts(i,:)=nan(s2,4);
        %find neighbours and put them in group then remove them from Pts
        s=s+s2;%update s so j would test all group member
%%%         ALL_DIRECTION MUST BE RUNAS MUCH AS SIZE(PTS,1)             %%%
    end
    m=m+1;
    
    s=s+1;
    l=find(isnan(Pts(:,1))==0,1,'first');
    Pts(1:l-1,:)=[];
end



% function group=separate(pt,Pts,dist)
% i=all_direction(pt,Pts,dist);
% s=size(i,1);
% group=nan(size(Pts));
% group(1:s,:)=Pts(i,:);
% Pts(i,:)=nan(s,4);
% if(s>0)
%     j=0;
%     while (j<s)
%         j=j+1;
%        
%         i=all_direction(group(j,:),Pts,dist);
%         s2=size(i,1);
%         group(s+1:s+s2,:)= Pts(i,:);
%         Pts(i,:)=nan(s2,4);
%         s=s+s2;
%         
%     end
% end
% s=s+1;
%     group(s,:)=[NaN NaN NaN NaN]; 
%     % first droplet done
% while(s<size(Pts,1))
%     l=find(isnan(Pts(:,1))==0,1,'first');
%     pt=Pts(l,:);
%     i=all_direction(pt,Pts,dist);
%     s2=size(i,1);
%     group(s+1:s+s2,:)= Pts(i,:);
%     j=j+1;
%     s=s+s2;
%     Pts(i,:)=nan(s2,4);
% if(s>0)
%     while (j<s)
%         j=j+1;
%         i=all_direction(group(j,:),Pts,dist);
%         s2=size(i,1);
%         group(s+1:s+s2,:)= Pts(i,:);
%         Pts(i,:)=nan(s2,4);
%         s=s+s2;     
%     end
%     
% end
% s=s+1;
%  group(s,:)=[NaN NaN NaN NaN]; 
% end
% 
% end
