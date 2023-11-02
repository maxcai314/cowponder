BUILD_DIR := .
INSTALL_DIR := /var/www/max/cowponder
COWTHOUGHTS := cowthoughts.txt

.PHONY: all install

all: install

install: $(BUILD_DIR)/$(COWTHOUGHTS)
	cp $< $(INSTALL_DIR)
