# [Outline](https://www.getoutline.com/) & [Albert](https://albertlauncher.github.io/) connector



## Adding albert-outline extension to pre-existing Albert installing

Coming soon....


## Installing from scratch (Albert + Albert-Outline extension)
### Ubuntu (Tested for 20.04)


```
curl "https://build.opensuse.org/projects/home:manuelschneid3r/public_key" | sudo apt-key add -
```


```
curl https://build.opensuse.org/projects/home:manuelschneid3r/public_key | sudo apt-key add -
echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_20.04/ /' | sudo tee /etc/apt/sources.list.d/home:manuelschneid3r.list
sudo wget -nv https://download.opensuse.org/repositories/home:manuelschneid3r/xUbuntu_20.04/Release.key -O "/etc/apt/trusted.gpg.d/home:manuelschneid3r.asc"
sudo apt update
sudo apt install albert
```