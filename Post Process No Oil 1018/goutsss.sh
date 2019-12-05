for i in `seq 4400 50 5300`
do
#i=12200
cp gouttes-$i.npy gouttes.npy
python count.py
mv gouttelettes.npy gouttelettes-$i.npy
done
