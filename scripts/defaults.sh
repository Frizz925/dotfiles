#!/bin/sh

defaults write -g ApplePressAndHoldEnabled -bool false
defaults write -g com.apple.mouse.scaling -1
defaults write com.apple.dock tilesize -int 32
defaults write com.apple.screencapture disable-shadow -bool true
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true

