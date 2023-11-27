CONTENTS_DIR := ./contents
BUILD_DIR := .
INSTALL_DIR := /var/www/max/cowponder
TARBALL_FILE := cowponder-homebrew-v0.0.3.tar.gz

PACKAGE_FILE := ../Formula/cowponder.rb

# ANSI color codes
BLUE := \033[0;34m
RESET := \033[0m

.PHONY: all clean install

all: $(BUILD_DIR)/$(TARBALL_FILE)

install: $(BUILD_DIR)/$(TARBALL_FILE)
	cp $^ $(INSTALL_DIR)

clean:
	rm -f $(BUILD_DIR)/$(TARBALL_FILE)

# build package and update checksum in ../Formula/cowponder.rb
$(BUILD_DIR)/$(TARBALL_FILE): $(CONTENTS_DIR)
	tar -czvf $@ -C $^ .

	new_checksum="$$(shasum -a 256 $@ | cut -d ' ' -f 1)" && \
	echo && printf "new checksum: $(BLUE)$$new_checksum$(RESET)\n" && echo && \
	awk -v new_checksum="$$new_checksum" 'BEGIN { found = 0 } { \
		if (found == 0 && $$1 == "sha256") { \
			print "  sha256 \"" new_checksum "\""; \
			found = 1; \
		} else { \
			print; \
		} \
	}' $(PACKAGE_FILE) > $(PACKAGE_FILE).temp && \
	mv $(PACKAGE_FILE).temp $(PACKAGE_FILE)

	@echo "updated new checksum in $(BLUE)../Formula/cowponder.rb$(RESET)"
