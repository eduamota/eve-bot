# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 15:44:26 2018

@author: aquic
"""

#%%
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config

training_data = load_data('Data_NLU/nlu.md')
trainer = Trainer(config.load("Config/config_spacy.yml"))
trainer.train(training_data)
model_directory = trainer.persist('./projects/')  # Returns the directory the model is stored in