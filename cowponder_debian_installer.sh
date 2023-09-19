#!/usr/bin/env bash
TEMP_DEB="$(mktemp)"
wget -O "$TEMP_DEB" 'https://xz.ax/cowponder_0.0.1-1_all.deb'
dpkg -i "$TEMP_DEB"
rm -f "$TEMP_DEB"
