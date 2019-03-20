mkdir -p paraevaluar_1.0-2/usr/local/bin
cp paraevaluar paraevaluar_1.0-2/usr/local/bin/

dpkg-deb --build paraevaluar_1.0-2
