# Robopi - build our robot

## Material



## Installation

After installing Raspberry OS in your PI, use `raspi-config` command to activate SSH, VNC and I2C interfaces

Next, setting up the Adafruit CRICKIT : switch of the Raspberry PI, attach the HAT to the PI, then, connect the CRICKIT to the HAT.
Finally, power on the PI, open a SSH terminal and run this followed command to check if the 0x49 address appears :

```
i2cdetect -y 1
```

Then, run the following lines to update your packages

```
sudo apt update
sudo apt upgrade
sudo apt autoremove
sudo reboot
```

After rebooting, create your Python virtual environnement and install Adafruit CRICKIT library :

```
python3 -m venv ~/pyenv
~/pyenv/bin/pip install adafruit-circuitpython-crickit
```

And create the environnement alias :

```
echo "alias activate='source ~/pyenv/bin/activate'" >> ~/.bashrc
```

### Install dependencies

```
pip install -r requirement.txt
```