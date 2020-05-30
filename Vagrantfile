# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
 # The most common configuration options are documented and commented below.
 # For a complete reference, please see the online documentation at
 # https://docs.vagrantup.com.

 # Every Vagrant development environment requires a box. You can search for
 # boxes at https://vagrantcloud.com/search.
 config.vm.box = "centos/7"
 config.vm.hostname = "django-centos7"
 # Setup port forwarding for httpd
 config.vm.network "forwarded_port", guest: 5000, host: 5000
 # Shared folder setting
 config.vm.synced_folder ".", "/vagrant", type: 'virtualbox'

 config.vm.provision "shell", inline: <<-SHELL
   sudo yum update -y
   sudo yum install -y python3
   touch /home/vagrant/.bash_aliases
   if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
     echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
     echo "alias python='python3'" >> /home/vagrant/.bash_aliases
   fi
  SHELL
end
