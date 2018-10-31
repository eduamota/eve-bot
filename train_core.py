# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:15:04 2018

@author: aquic
"""

#%%

# Imports
#-----------
# rasa core
import logging
from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy

#%%
# Function
#------------
def train_dialog(dialog_training_data_file, domain_file, path_to_model = 'models/dialogue'):
    logging.basicConfig(level='INFO')
    agent = Agent(domain_file,
              policies=[MemoizationPolicy(max_history=1)])
    training_data = agent.load_data(dialog_training_data_file)
    agent.train(
        training_data,
        augmentation_factor=50,
        epochs=200,
        batch_size=10,
        validation_split=0.2)
    agent.persist(path_to_model)


#%%
# Train
#--------
train_dialog('Data_Core/stories.md', 'Data_Core/domain.yml')