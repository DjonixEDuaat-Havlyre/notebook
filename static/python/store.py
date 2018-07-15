#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  store.py
#  
#  Copyright 2018 jh <jh@jh-tp430>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
'''
	Top installs by category
'''
import xml.etree.ElementTree as ET

class Tops(object):
	""" Favorite apps, plugs, etc """
	
	def __init__ (self, tree='/home/jh/Documents/tops/index.xml'):
		try:
			self.tree = ET.parse(tree)
			self.root = tree.getroot()
		except Exception, ex:
			raise ex
		finally:
			print("Init Complete")
	
	def nuthin(newthing=None):
		def _nuthin(nutin, typec):
			# add nutin as typec as needed
			self.root.get(iter_child_nodes, name
		if newthing:
			if type(newthing) is str:
				#newthing is a string, so add a new app by default
				_nuthin((newthing, 'app'))
			else:
				#newthing should be a tuple of (thing, typec)'s
				try:
					for nutin, typec in newthing:
						_nuthin(nutin, typec)
				except Exception, ex:
					raise ex
				finally:
					pass
		else:
			#newthing is None, 0, {}, or '' so return list of things
			pass
			
	
				
			
			

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
