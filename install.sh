#!/usr/bin/env bash
# Instagram-Profile-Downloader 1.2

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Please, Run This Programm as Root!"
  echo ""
  exit 1
fi
main() {
  printf '\033]2Instagram-Profile-Downloader\a';
  clear
  echo "Installing..."
  chmod +x start.py
  sleep 2
  apt install python
  apt install python3
  apt install python3-pip
  pip3 install --upgrade pip
  echo ""
  echo "Finish...!"
  echo ""
  exit 1
}
main