
function [index1,index2]=Alpha(XInterval,Y_Apply,Z_Apply,Ref_Pts,index1,index2)

while(logical(sum(index1~=index2)))    
   clear a;
index_in=index1&~index2;
Pts_In=Ref_Pts(index_in,:);
  index_out=false(size(index1));
A=decompose(Pts_In,XInterval);
  S=size(A,1);
  for i=1:S
    J=Pts_In(A(i,1):A(i,2),2);
    K=Pts_In(A(i,1):A(i,2),3);
    index_o=summation(Y_Apply,Z_Apply,A(i,:),J,K);
    index_out(A(i,3):A(i,4))=index_out(A(i,3):A(i,4)) | index_o;
  end
index1=index1 | index_out;
index2=index2 | index_in;

end
end


function index_o=summation(Y_Apply,Z_Apply,A,J,K)
SX=A(1,4)-A(1,3)+1;
max_ram=40;% suppose i have 10 GB to use
max_ram=int64(max_ram*1024*1024*1024/(4*size(J,1)));
    if(SX<max_ram)
    index_o=Y_Apply(A(1,3):A(1,4),J)&Z_Apply(A(1,3):A(1,4),K);
    index_o=logical(sum(index_o,2));
    else
        index_o=false(SX,1);
        j=1
        for i=A(1,3):max_ram:A(1,4)+1
            a(1,j)=i; j=j+1; 
        end
        a(1,j)=A(1,4)+1;
        for j=1:size(a,2)-1
        index_temp=Y_Apply(a(j):a(j+1)-1,J)&Z_Apply(a(j):a(j+1)-1,K);
        index_o(a(j)-A(1,3)+1:a(j+1)-A(1,3),:)= index_o(a(j)-A(1,3)+1:a(j+1)-A(1,3),:) | logical(sum(index_temp,2));
        end
    end
end