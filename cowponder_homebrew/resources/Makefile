CONTENTS_DIR := ./contents
BUILD_DIR := .
INSTALL_DIR := /var/www/html
TARBALL_FILE := cowponder-homebrew-v0.0.2.tar.gz

.PHONY: all clean install

all: $(BUILD_DIR)/$(TARBALL_FILE)

install: $(BUILD_DIR)/$(TARBALL_FILE)
	cp $(BUILD_DIR)/$(TARBALL_FILE) $(INSTALL_DIR)

$(BUILD_DIR)/$(TARBALL_FILE): $(CONTENTS_DIR)
	tar -czvf $(BUILD_DIR)/$(TARBALL_FILE) -C $(CONTENTS_DIR) .
	shasum -a 256 $(BUILD_DIR)/$(TARBALL_FILE)

clean:
	rm -f $(BUILD_DIR)/$(TARBALL_FILE)
