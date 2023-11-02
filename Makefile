BUILD_DIR := .
INSTALL_DIR := /var/www/max/cowponder
COWTHOUGHTS := cowthoughts.txt

DEBIAN_DIR := ./cowponder_debian
HOMEBREW_DIR := ./cowponder_homebrew/resources

.PHONY: all clean install

all:
	make -C $(DEBIAN_DIR) all
	make -C $(HOMEBREW_DIR) all
	@echo Please edit cowponder_homebrew/Formula/cowponder.rb and add new checksum.

clean:
	make -C $(DEBIAN_DIR) clean
	make -C $(HOMEBREW_DIR) clean

install: $(INSTALL_DIR)/$(COWTHOUGHTS)
	make -C $(DEBIAN_DIR) install
	make -C $(HOMEBREW_DIR) install

$(INSTALL_DIR)/$(COWTHOUGHTS): $(BUILD_DIR)/$(COWTHOUGHTS)
	cp $^ $@
