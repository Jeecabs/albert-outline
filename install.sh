# Removes the old installation (if it exists)
sudo rm -rf /usr/share/albert/org.albert.extension.python/modules/outline || true

cp outlineSearch.py outline/__init__.py

sudo cp -r outline /usr/share/albert/org.albert.extension.python/modules

# Deletes the generated file to prevent any confusion about duplicate files
rm outline/__init__.py
