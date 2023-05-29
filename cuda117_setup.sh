wget "https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin"
sudo mv cuda-wsl-ubuntu.pin "/etc/apt/preferences.d/cuda-repository-pin-600"
wget "https://developer.download.nvidia.com/compute/cuda/11.7.1/local_installers/cuda-repo-wsl-ubuntu-11-7-local_11.7.1-1_amd64.deb"
sudo dpkg -i "cuda-repo-wsl-ubuntu-11-7-local_11.7.1-1_amd64.deb"
sudo cp "/var/cuda-repo-wsl-ubuntu-11-7-local/cuda-*-keyring.gpg" "/usr/share/keyrings/"
rm cuda-repo-wsl-ubuntu-11-7-local_11.7.1-1_amd64.deb*
sudo apt-get update
sudo apt-get -y install cuda