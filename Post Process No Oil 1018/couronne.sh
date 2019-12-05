for i in `seq 4400 50 5300`
do
#i=12200
cp data-$i.npy data.npy
python Reconstruction.py
#mv couronne.txt couronne-$i.txt
#mv MainPts.txt MainPts-$i.txt
mv gouttes.npy gouttes-$i.npy
mv MainPts.npy MainPts-$i.npy 
#mv data.npy data-$i.npy
done
