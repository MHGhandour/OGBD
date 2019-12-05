
function neighbour=all_direction(pt,Pts,dist)
pt1=pt+[0 0 dist 0];
neighbour=findpoint(pt1,Pts);

pt1=pt+[0 dist 0 0];
neighbour=[neighbour; findpoint(pt1,Pts)];

pt1=pt+[dist 0 0 0];
neighbour=[neighbour; findpoint(pt1,Pts)];

pt1=pt+[0 0 -dist 0];
neighbour=[neighbour; findpoint(pt1,Pts)];

pt1=pt+[0 -dist 0 0];
neighbour=[neighbour; findpoint(pt1,Pts)];

pt1=pt+[-dist 0 0 0];
neighbour=[neighbour; findpoint(pt1,Pts)];


end