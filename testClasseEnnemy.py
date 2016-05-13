#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

class Ennemy():
	
	def __init__(self, life, level):
		self.life = life
		self.level = level

		
	def afficher(self):
		print(self.life, self.level)
	
	def attaque(self):
		print('BAM')
		self.life -= 1
		
	def check_life(self):
		if self.life <= 0:
			print('dead')
			
		else:
			print(str(self.life) + ' life point left')

ennemi1 = Ennemy(life = 54, level = 3)
ennemi1.afficher()

for i in range(3):
	ennemi1.attaque()
	ennemi1.check_life()


