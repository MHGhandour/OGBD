% %%
% pltgouttes2(Points2)
% 
% pltgouttes(Points)

%% The test below is so important i may add it to the article
% for i=1:6000
% findpoint(MainPts(1,:),MainPts(1:100000,:));
% end

%% The test below is so important i may add it to the article too
% B=cputime;
% A=zeros(8,2);
% for l=9:15
%     s=2^l;
% for i=1:s
% neighbours(Pts(1,:),Pts(1:s,:));
% end
% A(l-8,1)=s;
% A(l-8,2)=cputime-B;
% B=cputime;
% end
% 

%%
B=cputime;
A=zeros(10,2);
for l=9:18
    s=2^l;
Pts=MainPts(1:s,:);
Pts=Idlize(Pts);
Pts=intervalise(Pts);
tejmi3(Pts);
A(l-8,1)=s;
A(l-8,2)=cputime-B;
B=cputime;
end