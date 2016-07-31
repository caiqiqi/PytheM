#coding=utf-8
import sys
from subprocess import *
import time
import readline

class Completer(object):
	name = "TAB completer"
	desc = "Auto complete PytheM commands with tab"
	version = "0.3"


        def __init__(self,console):
        	# enable tab-completion
		tab = readline.parse_and_bind("tab: complete")
		if console == "pythem":
			completer = readline.set_completer(self.pythem)
			# Set or remove the completer function.
			# The function is called as function(text, state)

	def suboption(self, text, state):
		#print text
		#print state
		results = [x for x in self.suboptions if x.startswith(text)] + [None]
		return results[state]

	# It should return the next possible completion starting with 'text'.
    	def pythem(self, text, state):
    	#print text
	#print state
	# 只要按TAB键时，已经输入的字符串包含"set"，即便是"seta"也可以出现提示。
		if "set" in text and state == 1:
			self.suboptions = ['interface','arpmode','target','gateway','file','domain','port','script','redirect']
			completer = readline.set_completer(self.suboption)
		elif "jarvis" in text and state == 1:
			self.suboptions = ['help','log','say','read']
			completer = readline.set_completer(self.suboption)
		elif "print" in text and state == 1:
			self.suboptions = ['interface', 'arpmode', 'target', 'gateway','file']
			completer = readline.set_completer(self.suboption)
		elif "scan" in text and state == 1:
			self.suboptions = ['tcp','arp','manual']
			completer = readline.set_completer(self.suboption)
		elif "arpspoof" in text and state == 1:
			self.suboptions = ['start', 'stop','status']
			completer = readline.set_completer(self.suboption)
		elif "dnsspoof" in text and state == 1:
			self.suboptions = ['start','stop','status']
			completer = readline.set_completer(self.suboption)
		elif "inject" in text and state == 1:
			self.suboptions = ['start','stop','status']
			completer = readline.set_completer(self.suboption)
		elif "xploit" in text and state == 1:
			self.suboptions = ['stdin', 'tcp']
			completer = readline.set_completer(self.suboption)
		elif "brute-force" in text and state == 1:
			self.suboptions = ['ssh','url','form']
			completer = readline.set_completer(self.suboption)
		elif "dos" in text and state == 1:
			self.suboptions = ['mitmdrop','stop']
			completer = readline.set_completer(self.suboption)
		else:
	       		self.words = ['clear','help','exit','quit','set','print','scan','arpspoof','dnsspoof','inject','sniff','pforensic','dos','xploit','brute','geoip','decode','encode','cookiedecode','jarvis']
			results = [x for x in self.words if x.startswith(text)] + [None]
		return results[state]

