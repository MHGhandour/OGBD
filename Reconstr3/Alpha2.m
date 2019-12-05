
function [points1,points2]=Alpha2(X_Apply,Y_Apply,Z_Apply,Ref_Pts,points1,points2)
%while(logical(sum(points1~=points2)))    
points_in=points1&~points2;
    I=Ref_Pts(points_in,1);
    J=Ref_Pts(points_in,2);
    K=Ref_Pts(points_in,3);
    points_out=X_Apply(:,I)&Y_Apply(:,J)&Z_Apply(:,K);
  %
   points_out=logical(sum(points_out,2));size(points_out);
points1=points1 | points_out;
points2=points2 | points_in;
%end
end



