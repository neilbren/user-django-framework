#!/bin/bash

# Install python3 packages
yum install -y python3

# Create alias python='python3'
if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_profile; then
  echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_profile
  echo "alias python='python3'" >> /home/vagrant/.bash_profile
fi

# Reboot VM
reboot
