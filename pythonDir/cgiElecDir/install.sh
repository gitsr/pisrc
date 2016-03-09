export IDIR=/usr/local/bin/elec

sudo cp $IDIR/elec.py $IDIR/elec.py.old
sudo cp elec.py $IDIR

cp /var/www/elec/elec.html /var/www/elec/elec.html.old
cp elec.html /var/www/elec
