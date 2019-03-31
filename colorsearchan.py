#!/usr/bin/env python
# -*- coding: utf8 -*-
import fcntl
import glob #拡張しでフィルタ
import tkinter as tk
import tkinter.filedialog, tkinter.messagebox
from tkinter import ttk
from tkinter.colorchooser import *
import threading
from multiprocessing import freeze_support, set_start_method, Process
freeze_support()
import imagecolor as cl
import os
#from multiprocessing import Queue
import shutil
#tk.tkを継承している

class Root(tk.Tk):	
	#selfには継承したクラスもあてられている
	def __init__(self):
		super().__init__()
		
		
		self.title("Image Color Sea chan")
		self.minsize(500,400)
		self.maxsize(500,400)
		
		#self.thread_obj = Process(target = self.pushed2,args=(q,))
		
		self.thread_obj = threading.Thread(target = self.pushed2)

		self.label = tk.Label(self, text="色で検索したい画像が入ってるフォルダを選択してください", padx=1, pady=50)
		self.label.pack()
		
		self.folder_path = None
		self.selected_color = None
		self.isfinished = False

		self.button = tk.Button(self,text = "フォルダを選択する",command = self.pushed)
		self.button2 = tk.Button(self,text = "実行",command = lambda:self.thread_obj.start(),state = "disabled")
		#self.button2 = tk.Button(self,text = "実行",command = self.pushed2,state = "disabled")

		self.button3 = tk.Button(self,text='抽出したい画像の色を選択', command=self.getColor)
		self.button4= tk.Button(self,text='停止', command= self.finished, state = "disabled")
		
		self.canvas = tk.Canvas(self,width =300,height = 100)
		self.canvas.create_rectangle(0,0,290, 90,outline = "white")
		self.canvas.pack()
		
		self.label2 = tk.Label(self, text="現在選択している色", padx=1, pady=5)
		self.label2.pack()
		self.button3.pack()
		#ボタンの表示
		self.button.pack()
		self.button2.pack()
		self.button4.pack()

		#progressbar
		self.pb = ttk.Progressbar(
				orient = "horizontal",
				mode='determinate')
		self.pb.pack(fill = "both",anchor = "s", side = "bottom")
		
		self.mainloop()
		
	def finished(self):
		
		if not self.isfinished:
			self.isfinished = True
			tk.messagebox.showinfo('終了','処理が終了しました')
			self.thread_obj = None
			self.thread_obj = threading.Thread(target = self.pushed2)
			self.button2.configure(text = "実行",state = "normal",command = lambda:self.thread_obj.start())
			#self.button2.configure(text = "実行",state = "normal",command = self.pushed2)

			self.button.configure(state = "normal")
			self.button3.configure(state = "normal")
			self.button4.configure(state = "disabled")

	
	def pushed2(self):
		#フォルダが存在したら、
		if self.folder_path is not None:
			self.button2.configure(text = "実行中",state = "disabled")
			self.button.configure(state = "disabled")
			self.button3.configure(state = "disabled")
			self.button4.configure(state = "normal")
			self.isfinished = False
			self.a(self.folder_path,self.selected_color)
			
		else:
			tk.messagebox.showinfo('フォルダ選択','画像が入っているフォルダを選択してください')
			
	def bar_controll(self,amount):
		self.pb.step(amount)
		
		
	def pushed(self):
		#root.withdraw() #１個目のウィンドウが最小化される
		folder = tk.filedialog.askdirectory()
		self.folder_path = os.path.abspath(folder)
		self.button2.configure(state = "normal")
		progressbar_maximum = color.count_images(self.folder_path)
		self.pb.configure(maximum=progressbar_maximum)

		
	def getColor(self):
		self.selected_color = askcolor()
		self.canvas.create_rectangle(0,0,290, 90,fill = self.selected_color[1],outline = self.selected_color[1])
	
	#圧縮した画像を生成。
	def a(self,folder_path,selected_color):

		#if os.path.exists(folder_path + "/smalled"):
		#	shutil.rmtree(folder_path + "/smalled")
		#	print("smallフォルダをつくりなおすよ")
			
		image_number = color.count_images(folder_path)		
		#copied_folder = shutil.copytree(folder_path, folder_path + "/smalled")	
		
		if not os.path.exists(folder_path + "/smalled_images"): os.mkdir(folder_path + "/smalled_images")
		small_images_folder = folder_path + "/smalled_images"
		
		"フォルダ内のjpgとpngの配列"
		image_files_list = glob.glob(folder_path + "/*.jpg") + glob.glob(folder_path + "/*.png")	
		
		for image_file in image_files_list:
			shutil.copy(image_file, str(small_images_folder))
		
		#image_files = [item for item in os.listdir(folder_path) if item[-4:] == ".jpg" or item[-4:] == ".png"]
		
		#print(image_files)
		"""
		for item in os.listdir(folder_path):
			if item[-4:] == ".jpg" or item[-4:] == ".png":
				copied_folder = shutil.copy(folder_path +"/" +str(item), folder_path + "/smalled")	



		while True:
		
			for image_file in image_files:
				smalled_img = color.get_original_small_img(img_path= folder_path +"/" + str(image_file))
				smalled_img.save(copied_folder+ "/" + str(image_file))#smalledフォルダに低画質で複製,ファイル名同じ

				color.get_main_color_list_img(img_path = copied_folder +"/" + str(image_file),
											selected_color = selected_color,
											img_name = str(image_file),
											default_img_path=folder_path)					
				self.bar_controll(1)
				
				if self.isfinished:
					break
			
			break
		"""
		
		self.finished()	

if __name__ == "__main__":
	freeze_support()
	color = cl.Color()
	#メインウィンドウを作成
	root = Root()
