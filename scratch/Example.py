from ns3gym import ns3env

import argparse

startSim = False
iterationNum = 1
port = 5555
simTime = 5 # seconds
stepTime = 0.001  # seconds
seed = 0
simArgs = {"--simTime": simTime,
           "--stepTime": stepTime,
           "--testArg": 123}
debug = False

env = ns3env.Ns3Env(port=port, stepTime=stepTime, startSim=startSim,
                    simSeed=seed, simArgs=simArgs, debug=debug)
env.reset()


while True:
    action = agent.get_action(obs)
    obs, reward, done, info = env.step(action)

    if done:
        break
