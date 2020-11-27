# zctl
zctl "Zoom Control" is a collection of scripts for linux webcam routing. While designed for the video conference application Zoom, zctl works at the kernel level emulating a video input device so it will work on any video app.

### Functions
`zctl` is a tiny bash script for controlling the application.

`zctl start` will start the video capture and output devices, defaulting to pure video passthrough.
`zctl stop` will stop the aforementioned devices.
`zctl gui` brings up a little GTK GUI for controlling zctl.
`zctl status` displays the current selected output mode.

There are 3 current video routing modes.
`passthrough` will just pass the physical video device (webcam) to the virtual driver. Due to kernel magic this is done very quickly and shouldn't result in any noticeable latency (~3ms).

`video` will route the file `video.avi` to the output device in a loop.

`image` will show a static (non-moving) image specified in `image.jpg`.

Running `zctl routingmode` replacing "routingmode" with one of the routing modes above will switch zctl to that mode.

### Installation
#### On Debian
Debian 10 had a hard time loading the v4l2loopback kernel module, which I solved by disabling UEFI Secure Boot in the BIOS. It's also possible to manually sign the module if you with to keep Secure Boot enabled, but I won't get into that here.

```
sudo apt install python3 python3-pip python3-opencv v4l2loopback-utils
sudo depmod -a
sudo modprobe v4l2loopback

pip3 install numpy pillow
```

#### On ArchLinux
All dependencies currenly packaged in base ArchLinux repositories.

```
sudo pacman -S python3 opencv python-numpy python-pillow hdf5 v4l2loopback-dkms
sudo depmod -a
sudo modprobe v4l2loopback
```

You also might want to add an alias to `zctl` for easy access.

To test the output, ffmpeg provides the `ffplay` binary to view webcam output. `ffplay /dev/video0`

The GUI should work just fine without installing anything extra on most GTK platforms. If GTK isn't your thing, the cli utility provides all the functionality as the GUI.

It should go without saying, but zctl wont work on Windows or MacOS.


### Credits
jremmons for the pyfakewebcam library: https://github.com/jremmons/pyfakewebcam


### Contribution
PRs are always welcome. If you want to contact me directly feel free to shoot me an email.


### Disclaimer
Obviously don't use this to do anything that will get you in trouble. Your actions aren't my responsibility. This isn't a tool to get out of class. Stay safe and have fun!
