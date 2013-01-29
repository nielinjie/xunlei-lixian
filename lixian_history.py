import pickle
import os
import os.path
import lixian_config

from datetime import datetime

def add_history(url,action,info):
	#assert action in ('started','finished')
	history.append( (url,action,info,datetime.now()) )
	write_file()

def find_history_url(condition):
	return filter(  lambda tu:  condition(tu[0]),history)


def find_history_action(condition):
	return filter(  lambda tu:  condition(tu[1]),history)


def find_history_info(condition):
	return filter(  lambda tu:  condition(tu[2]),history)

def is_finished(url):
	return len(filter(lambda tu: tu[0]==url and tu[1]=='finished', history))!=0

def write_file() :
	history_file_w=open(history_path,'w')
	pickle.dump(history,history_file_w)

def read_file():
	if os.path.exists(history_path):
		history_file=open(history_path,'r')
		global history
		history=pickle.load(history_file)

history=[]
history_path=lixian_config.get_config_path('.xunlei.lixian.history')
read_file()