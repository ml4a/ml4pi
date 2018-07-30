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

Install pre-requisites for Tensorflow.

    sudo apt install libatlas-base-dev

Install tensorflow.

    pip3 install tensorflow

Install keras.

    pip3 install keras

Test your installation by running the following without errors:

    python3 -c "import tensorflow as tf;import keras"

Make sure you enable your camera through `sudo raspi-config`. Reboot again afterwards.

## Working with this library

Clone this library.

    git clone https://github.com/ml4a/ml4pi

Try running the interactive trainer.





### Sample dataset

Example is using a dataset which can be obtained:

    wget http://www.vision.caltech.edu/Image_Datasets/Caltech101/101_ObjectCategories.tar.gz
    tar -xzf 101_ObjectCategories.tar.gz