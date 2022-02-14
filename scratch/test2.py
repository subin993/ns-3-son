#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from ns3gym import ns3env
from action_func import*
from collections import OrderedDict
import numpy as np

__author__ = "Piotr Gawlowicz"
__copyright__ = "Copyright (c) 2018, Technische Universität Berlin"
__version__ = "0.1.0"
__email__ = "gawlowicz@tkn.tu-berlin.de"


startSim = False
iterationNum = 100
port = 5555
simTime = 5 # seconds
stepTime = 1  # seconds
seed = 0
simArgs = {"--simTime": simTime,
           "--stepTime": stepTime,
           "--testArg": 123}
debug = False

env = ns3env.Ns3Env(port=port, stepTime=stepTime, startSim=startSim,
                    simSeed=seed, simArgs=simArgs, debug=debug)
env.reset()

ob_space = env.observation_space
ac_space = env.action_space
print("Observation space: ", ob_space,  ob_space.dtype)
print("Action space: ", ac_space, ac_space.dtype)

stepIdx = 0
currIt = 0

try:
    while True:
        print("Start iteration: ", currIt)
        obs = env.reset()
        #New Part
        if(stepIdx<2):
            if(stepIdx==0):
                numOfenb = len(obs['dlPrbUsage'])
                threshold = 50
            else:
                numOfue = int(sum(obs['dlPrbUsage']))
                threshold = (100//numOfue)+15
        #Trasfer UeNum in eNB to PRB Usage
        if(stepIdx!=0):
            for i in range(numOfenb):
                obs['dlPrbUsage'][i] = round((obs['dlPrbUsage'][i]/numOfue)*100,2)
        print("Step: ", stepIdx)
        print("---obs: ", obs)
        

        while True:
            stepIdx += 1

            #New Part
            if(stepIdx==1):
                prev_action = OrderedDict()
                prev_action['Offset'] = []
                prev_action['Step'] = []
                for i in range(numOfenb):
                    prev_action['Offset'].append(6)
                    prev_action['Step'].append(0)

            
            action = action_func(obs,prev_action,numOfenb,threshold)
            prev_action = action
            action = OrderedDict()
            action['Offset'] = prev_action['Offset']

            print("---action: ", action)

            print("Step: ", stepIdx)
            obs, reward, done, info = env.step(action)
            print("---obs, reward, done, info: ", obs, reward, done, info)
            dlPrbUsage = obs["dlPrbUsage"]
            
            print("---dlPrbUsage: ", dlPrbUsage)
            

            if done:
                stepIdx = 0
                if currIt + 1 < iterationNum:
                    env.reset()
                break

        currIt += 1
        if currIt == iterationNum:
            break

except KeyboardInterrupt:
    print("Ctrl-C -> Exit")
finally:
    env.close()
    print("Done")
