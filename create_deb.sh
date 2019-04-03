mkdir -p paraevaluar_2.1-0/usr/local/bin
cp paraevaluar paraevaluar_2.1-0/usr/local/bin/

dpkg-deb --build paraevaluar_2.1-0
