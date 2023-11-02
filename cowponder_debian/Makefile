BUILD_DIR := .
INSTALL_DIR := /var/www/max/cowponder
DEB_CONTENTS_DIR := ./cowponder_0.0.1-1_all
DEB_FILE := cowponder_0.0.1-1_all.deb
INSTALLER_FILE := cowponder_debian_installer.sh

.PHONY: all clean install

all: $(BUILD_DIR)/$(DEB_FILE)

install: $(BUILD_DIR)/$(DEB_FILE) $(BUILD_DIR)/$(INSTALLER_FILE)
	cp $^ $(INSTALL_DIR)

$(BUILD_DIR)/$(DEB_FILE): $(DEB_CONTENTS_DIR)
	dpkg --build $^ $@

clean:
	rm -f $(BUILD_DIR)/$(DEB_FILE)
