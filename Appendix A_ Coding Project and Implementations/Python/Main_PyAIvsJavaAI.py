import os

os.chdir("D:\Desktop\FTG4.50\python")

import sys
from time import sleep
from py4j.java_gateway import JavaGateway, GatewayParameters, CallbackServerParameters, get_field
from KickAI import KickAI
from HtnAI_rapid_replanning import HtnAI #change to other imports
from machete import Machete



def check_args(args):
	for i in range(argc):
		if args[i] == "-n" or args[i] == "--n" or args[i] == "--number":
			global GAME_NUM
			GAME_NUM = int(args[i+1])

def start_game(ai, GAME_NUM):

		manager.registerAI("HtnAI", HtnAI(gateway))
		print("Start game", ai)
		game = manager.createGame("ZEN", "ZEN", "HtnAI", ai, GAME_NUM)
		manager.runGame(game)
	
		print("\nAfter game", ai)
		sys.stdout.flush()

def close_gateway():
	gateway.close_callback_server()
	gateway.close()
	
def main_process():
	check_args(args)
	start_game()
	close_gateway()





print("TRIAL 1 #################################################################")

AIs = ["ReiwaThunder", "JayBot_GM", "MrAsh"]


for ai in AIs:
	args = sys.argv
	argc = len(args)
	GAME_NUM = 3
	gateway = JavaGateway(gateway_parameters=GatewayParameters(port=4242), callback_server_parameters=CallbackServerParameters());
	manager = gateway.entry_point
	#check_args(args)
	start_game(ai, GAME_NUM)
	close_gateway()
