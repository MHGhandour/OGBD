function [MainPts,DenserPts]=letplainonly(MainPts)
j=(MainPts(:,4)==0);
MainPts(j,:)=[];
% i=(MainPts(:,4)~=1);
%     DenserPts=MainPts(i,:);
%     MainPts(i,:)=[];
end
    
% 
% function [MainPts,DenserPts]=letplainonly(MainPts)
% j=(MainPts(:,4)==0);
% MainPts(j,:)=[];
% i=(MainPts(:,4)~=1);
%     DenserPts=MainPts(i,:);
%     MainPts(i,:)=[];
% end
%     