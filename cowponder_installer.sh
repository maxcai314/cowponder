#!/usr/bin/env bash
TEMP_DEB="$(mktemp)"
wget -O "$TEMP_DEB" 'https://xz.ax/cowponder_0.0.1-1_all.deb'
dpkg -i "$TEMP_DEB"
rm -f "$TEMP_DEB"
echo
echo "cowponder may not be runnable as root, because the location of the cowthink runnable may not be in the sudo secure path."
