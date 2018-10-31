# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:07:53 2018

@author: aquic
"""

#%%

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
#from rasa_core.utils import AvailableEndpoint


#%%
#_endpoint = vailableEndpoints.read_endpoints(cmdline_args.endpoints)

interpreter = RasaNLUInterpreter("projects/default/model_20181029-224355/")

agent = Agent.load("models/dialogue", interpreter=interpreter)

#%%

i = input(">> ")

while i != "exit":
    print(agent.handle_text(i)[0]['text'])
    i = input(">> ")