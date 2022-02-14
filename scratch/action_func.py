from collections import OrderedDict


def action_func(obs,prev_action,numOfenb):
    action = OrderedDict()
    dlPrbUsage = obs['dlPrbUsage']
    off = prev_action['Offset']
    step = prev_action['Step']
    #New Part
    for i in range(numOfenb):
        if off[i] > -24 :
            if dlPrbUsage[i] >= 20:
                if off[i] > -6:
                    off[i] -= 1
                else:
                    off[i] -=2
                if step[i] ==1:
                    step[i] = 0
            if dlPrbUsage[i] <20:
                step[i] +=1
                if step[i]==2:
                    if off[i] <-6:
                        off[i] +=2
                    elif off[i] <6:
                        off[i] +=1
                    else:
                        off[i] +=2
                    step[i]=0

    action['Offset'] = off
    action['Step'] = step
    
    return action