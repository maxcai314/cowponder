#!/usr/bin/env bash

TEMP_DEB="$(mktemp)"

curl -o "$TEMP_DEB" -f -L 'https://max.xz.ax/cowponder/cowponder_0.0.1-1_all.deb' || { echo "error: Failed to download DEB file"; echo "cleaning up $TEMP_DEB"; rm -f "$TEMP_DEB"; exit 1; }
dpkg -i "$TEMP_DEB"
apt --fix-broken install --yes
rm -f "$TEMP_DEB"
chmod 666 '/etc/cowthoughts.txt'
