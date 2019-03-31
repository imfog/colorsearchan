#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import cv2
import imp
import multiprocessing
multiprocessing.freeze_support()
import sklearn.neighbors.typedefs
import sklearn
from sklearn.cluster import KMeans
from PIL import Image
import os,re
import numpy
#OpenCV、読み込んだままだとカラーチャンネルの順番がRGBになっていないようなので変換をしておきます。
class Color:
	def get_main_color_list_img(self,img_path,selected_color,img_name,default_img_path):
		
		cv2_img = cv2.imread(img_path)
		cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
		cv2_img = cv2_img.reshape((cv2_img.shape[0] * cv2_img.shape[1], 3))

		cluster = KMeans(n_clusters=4)
		cluster.fit(X=cv2_img)
		cluster_centers_arr = cluster.cluster_centers_.astype(int, copy=False)
		
		#4回繰り返す
		for rgb in cluster_centers_arr:
			
			image_rgb = numpy.array(rgb)
			color_rgb = numpy.array(selected_color[0])

			#絶対値を求める
			zettai = abs(image_rgb -color_rgb)
			
			if all((40 >= zettai)):
				#print(zettai)
				img = Image.open(fp = default_img_path +"/" + img_name)
				img.show()
				break
				
	def get_original_small_img(self,img_path):

		img = Image.open(fp=img_path)
		width = int(img.size[0] / 7)
		height = int(img.size[1] / 7)
		img = img.resize(size=(width, height))
		return img
		
	def count_images(self,folder_path):
		files = os.listdir(folder_path)
		count = 0
		for file in files:
			index = re.search(".jpg", file)
			if index:
				count +=1
				
			index = re.search(".png", file)
			if index:
				count +=1

		return count