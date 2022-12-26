# Ruthenia-UAV-to-OM
several channels (uav data) table look up python extention for oasis montaj

So to test this extention you need:
1. Load python menu to Oasis Montaj (https://geosoftgxdev.atlassian.net/wiki/spaces/GXD93/pages/102924426/Python+Installation+and+Configuration)
2. Download files from this repo, put "AGP_UAVtoOM.omn" to "omn" folder ("C:\Users\ruthenia\Documents\Geosoft\Desktop Applications 9\omn" in my case),
put "test_extentions.py" to "python" folder ("C:\Users\ruthenia\Documents\Geosoft\Desktop Applications 9\python" in my case), open "test.gdb" in Oasis.
3. Load AGP menu with "Manage Menus" in project explorer.
4. Choose "Test" in AGP menu, choose file via Browse button, then choose channel you want to write data in dropdown menu, then push "Do" button.
5. Enjoy result.

NB: Right now programm work only with certain test database and text file, but you can modify data in param column in text file.
