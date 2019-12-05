%script that take Points representing droplets separted by NaNs, then plot
%them seperatly.
function pltgouttes(Points)
figure
hold on;
M=max(Points(:,8));
m=1;
while (m<M)
I= Points(:,8)==m;
goutte=Points(I,:);
    plt(goutte,'.')
   drawnow
    clear goutte
    m=m+1;
end
hold off   
end