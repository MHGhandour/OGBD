%NOTE: I may add a way to minimize memory usage by giving each XInterval an
%ID, then give each point that ID.
function [XInterval,Y_Apply,Z_Apply,Ref_Pts]=idlize_interval(XInterval,YInterval,ZInterval,Ids)
s1=Ids(end,1);
%temp=Interval_Id(XInterval);
[X,XInterval]=X_Interval_Id(XInterval);

[Y,Id_ref]=Interval_Id(YInterval);
Id_ref=transpose(Id_ref(:,2:3));
Y_Apply=Fill(Id_ref,s1);
Y_Apply=Y_Apply(Ids(:,2),:);Y=Y(Ids(:,2),:);
[Z,Id_ref]=Interval_Id(ZInterval);
Id_ref=transpose(Id_ref(:,2:3));
Z_Apply=Fill(Id_ref,s1);
Z_Apply=Z_Apply(Ids(:,3),:);Z=Z(Ids(:,3),:);
Ref_Pts=[X Y Z];
end


function [YZ,Id_ref]=Interval_Id(YZPts)

i=1;s=size(YZPts,1);m=1;
Id_ref(i,:)=[m YZPts(i,:)];YZ(i,1)=m;
for i=2:s
    if(YZPts(i,1)~=YZPts(i-1,1) || YZPts(i,2)~=YZPts(i-1,2))
        m=m+1;Id_ref=[Id_ref; m YZPts(i,:)];
    end
    YZ(i,1)=m;
end
end

function Apply=Fill(Id_ref,s1)
s2=size(Id_ref,2);
Apply=false(s1,s2);
for i=1:s2
   Apply(Id_ref(1,i):Id_ref(2,i),i)=true(Id_ref(2,i)-Id_ref(1,i)+1,1);     
end
end


function [X,XInterval]=X_Interval_Id(XPts)

i=1;s=size(XPts,1);m=1;
XInterval=XPts(i,:);X(i,1)=m;
for i=2:s
    if(XPts(i,1)~=XPts(i-1,1) || XPts(i,2)~=XPts(i-1,2))
        m=m+1;   XInterval=[XInterval; XPts(i,:)];
    end
X(i,1)=m;
 
end
end