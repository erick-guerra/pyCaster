import time
import json
import logging
import pychromecast
from pychromecast.controllers.youtube import YouTubeController

class pyCaster:
	def __init__(self):
		# TODO: Move to its own update function
		self._chromecast_devices = pychromecast.get_chromecasts()
		self.deviDB = self.current = {}
		self.devi = []

	def get_devices(self):
		# logging.info('%s device was found !', self._chromecast_devices)
		# NOTE: In windows, pychromecast returns a tupple. Will need to make
		# OS gate checks.
		counter = 0
		for device in self._chromecast_devices:
			self.current[device.device.friendly_name] = {'option': str(counter),
										   'Model': device.model_name,
										   'Manufacturer': device.device.manufacturer,
										   'IP': device.host,
										   'Port': device.port,
										   'UUID': str(device.uuid),
										   'type': device.cast_type}
			counter += 1

	def set_device(self):
		dev = int(input("Enter Option Number: \n"))
		# Need to find index of selection from deviDB to set device
		self.devi = self._chromecast_devices[dev]

	def push_mp4_video(self, url):
		mc = self.devi.media_controller
		self.devi.wait()
		mc.play_media(url, 'video/mp4')

	def push_youtube_video(self, youtube_id):
		# TODO: Look up YoutubeCOntroller API
		# yt = YouTubeController()
		# self.devi.register_handler(yt)
		# yt.play_video(youtube_id)



# cast = next(cc for cc in chromecasts if cc.device.friendly_name == "Office TV")
# cast.wait()
# print(cast.device)
# mc = cast.media_controller
# mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')