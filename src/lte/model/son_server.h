#ifndef MY_GYM_ENTITY_H
#define MY_GYM_ENTITY_H

#include "ns3/lte-enb-net-device.h"
#include "ns3/lte-enb-rrc.h"

#include "ns3/opengym-module.h"
#include "ns3/nstime.h"
#include "ns3/ff-mac-scheduler.h"

namespace ns3{

class SonServerGymEnv: public OpenGymEnv {
    // friend class LteEnbNetDevice;
    // friend class LteEnbRrc;

    public:
        SonServerGymEnv();
        SonServerGymEnv(Time stepTime);

        virtual ~SonServerGymEnv();
        static TypeId GetTypeId (void);
        virtual void DoDispose();

        void AddNewNode(uint16_t cellId, Ptr<LteEnbNetDevice> dev);

        Ptr<OpenGymSpace> GetActionSpace();
        Ptr<OpenGymSpace> GetObservationSpace();
        bool GetGameOver();
        Ptr<OpenGymDataContainer> GetObservation();
        float GetReward();
        

        std::string GetExtraInfo();

        bool ExecuteActions(Ptr<OpenGymDataContainer> action);

        void ScheduleNextStateRead();
        Time m_interval;
        std::map<uint32_t, Ptr<LteEnbNetDevice> > m_enbs;
        
};

}
#endif