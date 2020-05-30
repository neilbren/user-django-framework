# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

# CentOS 7 VM

Vagrant.configure("2") do |config|
 # The most common configuration options are documented and commented below.
 # For a complete reference, please see the online documentation at
 # https://docs.vagrantup.com.

 # Every Vagrant development environment requires a box. You can search for
 # boxes at https://vagrantcloud.com/search.

 # launch latest Centos7 VM && update hostname
 config.vm.box = "centos/7"
 config.vm.hostname = "django-centos7"

 # Setup port forwarding for httpd
 config.vm.network "forwarded_port", guest: 5000, host: 5000

 # Create bilatoral sync between host and guest
 config.vm.synced_folder ".", "/vagrant", type: 'virtualbox'

 # Update all packages && install python
 config.vm.provision "shell", inline: <<-SHELL
   sudo yum update -y
  SHELL

  # create python virtual environment
  config.vm.provision :shell, :path => "venv-bootstrap.sh"

end
