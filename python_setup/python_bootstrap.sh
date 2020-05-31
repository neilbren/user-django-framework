#!/bin/bash

set -e

# Install python3 packages
yum install -y python3

# Create alias python='python3'
touch /home/vagrant/.bash_aliases
if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bashrc; then
  echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bashrc
  echo "alias python='python3'" >> /home/vagrant/.bashrc
fi

# create python virtual environment
cd /vagrant/; python -m venv ~/env
source ~/env/bin/activate
pip -V > ~/venv_install_path.txt
pip install --upgrade pip

# Install django framework
pip install -r /vagrant/python_setup/requirments.txt
if [ $? -gt 0 ]; then
    echo 2> 'Unable to install django framework requirements from requirements.txt file!'
    exit 1
fi

# Reboot VM
reboot
