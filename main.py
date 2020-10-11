import time
import json
import logging
import pychromecast
from pychromecast.controllers.youtube import YouTubeController

# TODO: Create formated printing of device listing

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
			self.current[device.device.friendly_name] = {
				'option': str(counter),
				'Model': device.model_name,
				'Manufacturer': device.device.manufacturer,
				'IP': device.host,
				'Port': device.port,
				'UUID': str(device.uuid),
				'type': device.cast_type
			}
			counter += 1

	def set_device(self):
		dev = int(input("Enter Option Number: \n"))
		# Need to find index of selection from deviDB to set device
		self.devi = self._chromecast_devices[dev]

	def push_mp4_video(self, url):
		# TODO: test to see if localy hosted files work
		mc = self.devi.media_controller
		self.devi.wait()
		mc.play_media(url, 'video/mp4')

	def push_youtube_video(self, youtube_id):
		''' Will not work fot 'Audio Cast' type devices, neet to create warning and
		 get ready to catch some warnings'''
		
		# Establsihes device instance to chromecast module
		yt = YouTubeController()
		mc = pychromecast.Chromecast(self.devi.host)
		mc.register_handler(yt)
		# Have to add wait to establish connection
		mc.wait()
		yt.play_video(youtube_id)
