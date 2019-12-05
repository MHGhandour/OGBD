function points=Id_reference(points, axe1, axe2, Ids)
column=3*(axe1-1)+axe2;
points=Ids(points,column);
end