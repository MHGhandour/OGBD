function Pts=Id_gathering(Pts,Ref_Pts,XInterval,Y_Apply,Z_Apply)
S=size(Ref_Pts,1);m=1;L=1;
%S2=size(Y_Apply,2);
%hold on;
while(size(L,1)>0)
points1=false(S,1);points1(L,1)=true;
GPts=Alpha(XInterval,Y_Apply,Z_Apply,Ref_Pts,points1,false(S,1));
SZ=sum(GPts);
Ref_Pts(GPts,:)=nan(SZ,3);
Pts(:,6)=Pts(:,6)+m.*GPts;
m=m+1;
%plt(Pts(GPts,:),'.');
%drawnow;%pause;
L=find(~isnan(Ref_Pts),1,'first');
end
end





















% 
% function points = indexezz(I,J,K, X_Apply,Y_Apply, Z_Apply)
% points=X_Apply(:,I)&Y_Apply(:,J)&Z_Apply(:,K);
% points=find(points);
% points(100)=0;
% end