for i in `seq 4400 50 5300`
do
gunzip sim-$i-*
gerris3D -e "GfsOutputSimulation {} text.txt {format = text}" sim-$i-* > /dev/null
python read.py
mv data.npy data-$i.npy
#gzip sim-$i-*
done
