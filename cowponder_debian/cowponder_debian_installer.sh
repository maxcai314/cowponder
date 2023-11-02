#!/usr/bin/env bash
TEMP_DEB="$(mktemp)"
wget -O "$TEMP_DEB" 'https://max.xz.ax/cowponder_0.0.1-1_all.deb'
dpkg -i "$TEMP_DEB"
apt --fix-broken install --yes
rm -f "$TEMP_DEB"
