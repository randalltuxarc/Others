#!/bin/bash
###########################################################
## 			    Openbox Installer by Randalltux              ##
##			     email: randalltux@yahoo.co.id               ##
##               twitter: @randalltux                    ##
###########################################################
# Reference http://forum.ubuntu-fr.org/viewtopic.php?id=399144
# run this script with sudo
# ex: sudo sh openbox-installer.sh
# This scripts it's just for KALI LINUX or ROOT USER ONlY!!!!
# Please fork this scripts
# Include: Numix Gtk themes, Numix-Circle icons , tint2rc numix , some wallpaper from numix
# Thanks to: MyBeloved @Putriayuerlyn , M.Claudio Delvin aka Cyberking , Iyan_Squid aka XBoot , @yogo_arp , Black Orion,
#                           Etc Session , Bagas Purwohandoyo , Aldy Torvalds aka alpoah , and YOU!
## Updating repository
echo "Updating Repositories"
apt-get update && apt-get upgrade
echo 'Update success'

## Installing openbox and supporting applications
echo "Installing openbox and supporting applications"
apt-get install openbox lxappearance thunar obmenu nitrogen tint2 xcompmgr xfce4-power-manager git git-core geany ttf-droid
echo "Install success with no errors =)"

## Installing compton and configuring cb-compositor
echo "Download & installing compton"
wget https://www.dropbox.com/s/kwhnm6orka6r8qf/compton-git_20120926-1_amd64.deb && dpkg -i compton-git_20120926-1_amd64.deb

echo "Installing & Configuring compton success"

## Configuring openbox , autostart , menu
echo "Create Openbox directory"
mkdir -p ~/./openbox/ && cd ~/.config/openbox
echo "Copying autostart file"
wget https://raw.githubusercontent.com/randalltuxarc/Openbox-installer/master/misc/openbox-autostart -O autostart
echo "Copying rc.xml"
wget https://raw.githubusercontent.com/randalltuxarc/Openbox-installer/master/misc/openbox-rc.xml -O rc.xml
echo "Copying menu.xml"
wget https://raw.githubusercontent.com/randalltuxarc/Openbox-installer/master/misc/menu.xml -O menu.xml
echo "Copying file success"

## Configuring tint2 panel, themes and icons from numix
echo "Downloading themes"
wget https://launchpad.net/~numix/+archive/ppa/+files/numix-gtk-theme_1.9~precise.tar.gz && tar xvfz numix-gtk-theme_1.9~precise.tar.gz && cd numix-gtk-theme && sudo mv Numix /usr/bin
echo "Themes installed"
echo "Downloading icons"
git clone https://github.com/numixproject/numix-icon-theme-circle.git && cd numix-icon-theme-circle && sudo mv Numix-Circle /usr/share/icons
echo "Icons installed"
echo "Configuring tint2 panel"
mkdir ~/.config/tint2 && cd ~/.config/tint2 && wget https://raw.githubusercontent.com/randalltuxarc/Openbox-installer/master/misc/tint2rc && cd /root
echo "Tint2 installed"
wget https://raw.githubusercontent.com/randalltuxarc/Openbox-installer/master/misc/gtkrc-2.0 -O .gtkrc-2.0

## Complete
echo "Your openbox has been installed.. Now logout and login to Openbox as your WM :)"

