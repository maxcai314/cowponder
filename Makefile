MAIN_DIR := .
INSTALL_DIR := /var/www/max/cowponder

DEBIAN_COWTHOUGHTS_DIR := ./cowponder_debian/cowponder_0.0.1-1_all/etc
HOMEBREW_COWTHOUGHTS_DIR := ./cowponder_homebrew/resources/contents

DEBIAN_DIR := ./cowponder_debian
HOMEBREW_DIR := ./cowponder_homebrew/resources

COWTHOUGHTS := cowthoughts.txt

TARGETS := $(INSTALL_DIR)/$(COWTHOUGHTS) $(DEBIAN_COWTHOUGHTS_DIR)/$(COWTHOUGHTS) $(HOMEBREW_COWTHOUGHTS_DIR)/$(COWTHOUGHTS)

.PHONY: update all clean install

update: $(DEBIAN_COWTHOUGHTS_DIR)/$(COWTHOUGHTS) $(HOMEBREW_COWTHOUGHTS_DIR)/$(COWTHOUGHTS)
	@echo Updated the default copy of cowthoughts.txt in Homebrew and Debian
	@echo Please make all install to publish changes

all:
	make -C $(DEBIAN_DIR) all
	make -C $(HOMEBREW_DIR) all

clean:
	make -C $(DEBIAN_DIR) clean
	make -C $(HOMEBREW_DIR) clean

install: $(INSTALL_DIR)/$(COWTHOUGHTS)
	make -C $(DEBIAN_DIR) install
	make -C $(HOMEBREW_DIR) install

$(TARGETS): $(MAIN_DIR)/$(COWTHOUGHTS)
	cp $^ $@
