wget -qO - http://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -
echo "deb http://dl.bintray.com/kusti8/chromium-rpi jessie main" | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install chromium-browser rpi-youtube -y


or

wget -qO - http://bintray.com/user/downloadSubjectPublicKey?username=bintray
sudo apt-key add -
echo "deb http://dl.bintray.com/kusti8/chromium-rpi jessie main"
sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install chromium-browser rpi-youtube -y


or

sudo apt-get install chromium-browser

sudo apt-get install ttf-mscorefonts-installer
