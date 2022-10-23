import cv2
import os
import json

from pynput import keyboard
from pynput.keyboard import Listener as KeyboardListener


def click_event(event, x, y, flags, params):

	if event == cv2.EVENT_LBUTTONDOWN:

		if img_name not in list(loc_dic.keys()):
			loc_dic[img_name] = {}
			loc_dic[img_name]['P'] = []
			loc_dic[img_name]['N'] = []

		loc_dic[img_name][class_key].append((x, y))

		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.rectangle(img, (x - SIZE, y - SIZE), (x + SIZE, y + SIZE), COLOR_DIC[class_key], 1)
		cv2.imshow(img_name, img)


def on_press(key):

	global image_index
	global quit
	global class_key
	global skip_image
	global loc_dic
	if 'char' in dir(key):
		if key.char == 'p':
			class_key = 'P'

		elif key.char == 'n':
			class_key = 'N'

		elif key.char == 's':
			skip_image = 1-int(skip_image)
			skip_image = skip_image == 1

	else:
		if key == keyboard.Key.esc:
			quit = True

		elif key == keyboard.Key.right:
			image_index += 1

		elif key == keyboard.Key.left:
			image_index -= 1

		elif key == keyboard.Key.down:
			image_index = len(list(loc_dic.keys()))

		elif key == keyboard.Key.up:
			image_index = 0

		class_key = 'P'

	return False

def load_location_dic():

	if SEGMENT_LOCATION_FILENAME.split('/')[-1] not in os.listdir():
		return {}

	else:
		with open(SEGMENT_LOCATION_FILENAME, 'r') as file:
			loc_dic = json.load(file)

		return loc_dic


if __name__ == '__main__':

	IMAGE_FOLDER = './data'
	SEGMENT_LOCATION_FILENAME = './segment_locations.json'
	COLOR_DIC = {'P': (0,0,0), 'N': (0,0,256)}
	loc_dic = load_location_dic()
	class_key = 'P'
	SIZE = 14
	quit = False
	image_index = len(list(loc_dic.keys()))
	skip_image = True

	while not quit:

		img_name = os.listdir(IMAGE_FOLDER)[image_index]

		img = cv2.imread(IMAGE_FOLDER + '/' + img_name)

		if img_name in loc_dic.keys():
			
			if len(loc_dic[img_name]['P']) > 0:
				for (x, y) in loc_dic[img_name]['P']:
					cv2.rectangle(img, (x - SIZE, y - SIZE), (x + SIZE, y + SIZE), (0,0,0), 1)
			if len(loc_dic[img_name]['N']) > 0:
				for (x, y) in loc_dic[img_name]['P']:
					cv2.rectangle(img, (x - SIZE, y - SIZE), (x + SIZE, y + SIZE), (0,0,256), 1)

		cv2.imshow(img_name, img)

		cv2.setMouseCallback(img_name, click_event)

		cv2.waitKey(0)

		cv2.destroyAllWindows()

		with KeyboardListener(on_press=on_press) as keyboard_listener:
			keyboard_listener.join()

	with open(SEGMENT_LOCATION_FILENAME, 'w') as file:
		file.seek(0)
		json.dump(loc_dic, file)