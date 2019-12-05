% Take Intervals, and point position and axe
% get interval point in a segment refered to that axe 
function points=interval(Intervals,axe,i)
column=1+3*(axe-1);
points=[Intervals(i,column+1) Intervals(i,column+2)];
%points=Intervals(inter, column);
end