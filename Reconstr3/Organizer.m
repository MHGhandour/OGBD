function MainPts=Organizer(file)
Pts=readtable(file,'Delimiter',' ');
Pts=Pts{:,[1 3 2 31 17:25]};
MainPts=letplainonly(Pts);
%%
MainPts(:,14)=0*MainPts(:,5)+1*MainPts(:,6)+2*MainPts(:,7)+3*MainPts(:,8)+4*MainPts(:,9)+5*MainPts(:,10)+6*MainPts(:,11)+7*MainPts(:,12)+8*MainPts(:,13);
MainPts(:,5)=MainPts(:,14);
MainPts(:,6:14)=[];
MainPts(:,1:3)=double(int16((MainPts(:,1:3)./(2.^(-MainPts(:,5))*ones(1,3)))*2))/2;
MainPts(:,1:3)=MainPts(:,1:3).*(2.^(-MainPts(:,5))*ones(1,3));
%%
MainPts=sortrows(MainPts,3);
MainPts=sortrows(MainPts,2);
MainPts=sortrows(MainPts,1);


end