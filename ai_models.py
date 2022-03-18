import os
import numpy as np
import tensorflow as tf

class DeepQNetwork(object):
    #building the q-network here
    def __init__(self, lr, n_action, name, fcl_dims = 256, input_dims=(210, 160,4)):
        self.lr = lr
        self.n_action = n_action
        self.name = name
        self.fcl_dims = fcl_dims
        self.input_dims = input_dims


    def build_net(self):

        # Model here
        return True

    def load_checkpoints(self):
        # Where we load the 
        return True

    def save_checkpoint(self):
        # Where we save previous instance
        return True

    class Agent(object):
        # building the model to move based off of the network.
        def __init__(self, name):
            self.name = name 

        def store_transaction(self, state, action, reward, state_, terminal):
            #storing the instances of the game
            return True

        def choose_action(self, state):
            # movement
            return True

        def learn(self):
            #how the model going to learn this
            return True