#!/usr/bin/env python
# -*- coding: utf-8 -*

from Tkinter import *
from PIL import Image, ImageTk
import os

class mygui():
	def __init__(self, image_dir, info_dir):
		self.root = Tk()
		self.root.title("Surgery Kit Detection")
		#self.root.geometry("500x500")
		
		self.find_images(image_dir)
		self.find_infos(info_dir)
		
		self.current_image = 0
		
		tkimg1 = self.ShowImg(self.images[self.current_image])
		self.PanelA = Label(self.root,image=tkimg1)
		self.PanelA.grid(row=0, column=0)
		tkimg2 = self.ShowImg(self.dets[self.current_image])
		self.PanelB = Label(self.root, image=tkimg2)
		self.PanelB.grid(row=0, column=1)
		
		self.text = Label(self.root, text='111')
		self.text,grid(row=3, columnspan=2)
		
		
		
		self.BtnPre = Button(self.root, text="Previous", command=self.select_previous)
		self.BtnNxt = Button(self.root, text="Next", command=self.select_next)
		self.BtnPre.grid(row=1, column=0, columnspan=2)
		self.BtnNxt.grid(row=2, column=0, columnspan=2)
		
		self.root.mainloop()
	
	def find_images(self, image_dir):
		self.images = []
		self.dets = []
		for currentName in os.listdir(image_dir):
			if 'det' in currentName:
				self.dets.append(os.path.join(image_dir, currentName))
			else:
				self.images.append(os.path.join(image_dir, currentName))
	
	def find_infos(self, info_dir):
		self.infos = []
		cnt = -1
		for f_name in os.listdir(info_dir):
			if "info" in f_name:
				cnt += 1
				self.infos.append([])
				with open(os.path.join(info_dir, f_name)) as f:
					for line in f:
						a,b,c,d = line.strip().split("+")
						self.infos[cnt].append([a,b,c,d])
	
	def ShowImg(self, img_dir):
		return ImageTk.PhotoImage(Image.open(img_dir))
	
	def refreshing(self):
		tkimg1 = self.ShowImg(self.images[self.current_image])
		self.PanelA.configure(image=tkimg1)
		self.PanelA.image = tkimg1
		tkimg2 = self.ShowImg(self.dets[self.current_image])
		self.PanelB.configure(image=tkimg2)
		self.PanelB.image = tkimg2
		
		
	
	def select_previous(self):
		if self.current_image > 0:
			self.current_image -= 1
			self.refreshing()
	
	def select_next(self):
		if self.current_image < len(self.images)-1:
			self.current_image += 1
			self.refreshing()

if __name__ == '__main__':
	mygui = mygui("images", "images")