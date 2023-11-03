CONTENTS_DIR := ./contents
BUILD_DIR := .
INSTALL_DIR := /var/www/max/cowponder
TARBALL_FILE := cowponder-homebrew-v0.0.2.tar.gz

.PHONY: all clean install

all: $(BUILD_DIR)/$(TARBALL_FILE)

install: $(BUILD_DIR)/$(TARBALL_FILE)
	cp $^ $(INSTALL_DIR)

$(BUILD_DIR)/$(TARBALL_FILE): $(CONTENTS_DIR)
	tar -czvf $@ -C $^ .
	shasum -a 256 $@
	new_checksum="$$(shasum -a 256 $@ | cut -d ' ' -f 1)" && \
	awk -v new_checksum="$$new_checksum" '{ \
		if ($$1 == "sha256") { \
			print "  sha256 \"" new_checksum "\""; \
		} else { \
			print; \
		} \
	}' ../Formula/cowponder.rb > ../Formula/cowponder_temp.rb && \
	mv ../Formula/cowponder_temp.rb ../Formula/cowponder.rb
	@echo updated new checksum in ../Formula/cowponder.rb

clean:
	rm -f $(BUILD_DIR)/$(TARBALL_FILE)
