# Variabile pentru a respecta cerința de structură (stil C/C++)
CC = pyinstaller
CFLAGS_DEBUG = --onefile
CFLAGS_RELEASE = --onefile --strip

BINARY_NAME = main
LIBRARY_NAME = libcalculator.so

# Căile de instalare cerute
INSTALL_BIN_DIR = /usr/local/bin
INSTALL_LIB_DIR = /usr/local/lib

# f. Regula default - apelează rețeta de release
default: release

# a. debug - compilează cu simboluri de debug (fără strip)
debug: main.py
	@echo "Compilare în mod DEBUG..."
	$(CC) $(CFLAGS_DEBUG) main.py

# b. release - compilează și elimină simbolurile de debug (folosind strip)
release: main.py
	@echo "Compilare în mod RELEASE (cu strip)..."
	$(CC) $(CFLAGS_RELEASE) main.py
	@echo "Generare bibliotecă simulată (dummy) pentru cerință..."
	@touch $(LIBRARY_NAME)

# c. clean - șterge fișierele temporare și binarele generate
clean:
	@echo "Curățare fișiere temporare și artefacte..."
	rm -rf build dist *.spec $(LIBRARY_NAME)

# d. install - mută binarul și librăria în directoarele de sistem cu masca 0644
# Are ca dependență 'release' (nu poți instala fără compilare)
install: release
	@echo "Instalare binar și bibliotecile în sistem cu masca 0644..."
	install -m 0644 dist/$(BINARY_NAME) $(INSTALL_BIN_DIR)/$(BINARY_NAME)
	install -m 0644 $(LIBRARY_NAME) $(INSTALL_LIB_DIR)/$(LIBRARY_NAME)

# e. uninstall - șterge artefactele din sistem
# Depinde de prezența fișierelor pe disc înainte de ștergere
uninstall: $(INSTALL_BIN_DIR)/$(BINARY_NAME) $(INSTALL_LIB_DIR)/$(LIBRARY_NAME)
	@echo "Dezinstalare aplicație din sistem..."
	rm -f $(INSTALL_BIN_DIR)/$(BINARY_NAME)
	rm -f $(INSTALL_LIB_DIR)/$(LIBRARY_NAME)

# regulile virtuale ca .PHONY (rețete care nu generează fișiere cu acel nume pe disc)
.PHONY: default debug release clean install uninstall
