# pyCaster

This is my initial deep dive into Chromecast API. My goal is to better understand the Chromecast API to have a higher level of control over Chromecast enabled devices. I plan to include this library into a toolset that provides control over other common IoT devices.

### Libraries used

pyCaster uses several open-source projects to work properly:

* [pychromecast] - A library for Chromecast by the makers of [home-assistant.io]
* [prettytable] - ASCII table print formater.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install prettytable, pychromecast
```

# Current Instance Functionality
  - List Chromecast enabled devices in the network
  - Set a specific device
  - Push valid mp4 URLs to cast/video-enabled device
  - Push youtube video to videocast type device

##### Future Features:
  -  Get status/information of media playing on specified device
  - Play/Pause/FFWD/RWND functionality for media playing
  - Cast locally hosted video/music/images to device
  - List and launch media type apps (Soundcloud, Pandora, etc)


### Todos

 - Add licensing to project
 - Add req file

### *A big 'thank you!' to:*
The entire [HAIO] team; [emontnemery] and [Balloob](https://pypi.org/user/balloob/) for laying down the foundation for my research.



   [pychromecast]: <https://github.com/home-assistant-libs/pychromecast>
   [prettytable]: <https://pypi.org/project/prettytable/>
   [HAIO]: <https://github.com/home-assistant>
   [home-assistant.io]: <https://www.home-assistant.io/>
   [emontnemery]: <https://pypi.org/user/emontnemery/>