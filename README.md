## Setup the Pi

Download the latest version of Raspbian and flash your micro SD card with [Etcher](https://etcher.io/)

Add blank file called `ssh` into the root of the SD disk and a file called `wpa_supplicant.conf` containing the following (replace with your wifi details):

    network={
        ssid="YOUR_WIFI_NETWORK"
        psk="YOUR_WIFI_PASSWORD"
    }
 

In terminal ssh into the pi:

    sudo ssh pi@raspberrypi.local

Default password is 'raspberry'. To change password use the `passwd` command.

Update the pi: 

    sudo apt-get update && sudo apt-get upgrade

Install nodejs:

    sudo apt-get install nodejs npm git-core

Optional: install nettalk for easy file sharing: 

    sudo apt-get install netatalk

Reboot:

    sudo reboot

## Install software

Install pre-requisites:

    sudo apt install libatlas-base-dev libjasper-dev libqtgui4 libqt4-test libhdf5-dev
	
Make sure you enable your camera through `sudo raspi-config`. Reboot again afterwards.

Clone this library:

    git clone https://github.com/ml4a/ml4pi

Install all the required python libraries:

	cd ml4pi
	pip3 install -r requirements.txt 

Try running the interactive trainer:

	python3 train_webcam.py


## Training a dataset from a folder of images

Example is using a dataset which can be obtained:

    wget http://www.vision.caltech.edu/Image_Datasets/Caltech101/101_ObjectCategories.tar.gz
    tar -xzf 101_ObjectCategories.tar.gz