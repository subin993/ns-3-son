#include "son_server.h"
#include "ns3/object.h"
#include "ns3/core-module.h"
#include "ns3/log.h"
#include "ns3/lte-enb-rrc.h"

#include <iostream>
#include <sstream>

namespace ns3{

    NS_LOG_COMPONENT_DEFINE ("SonServerGymEnv");

    NS_OBJECT_ENSURE_REGISTERED (SonServerGymEnv);

    SonServerGymEnv::SonServerGymEnv (){
        NS_LOG_FUNCTION(this);
        m_interval = Seconds(5);

        Simulator::Schedule (Seconds(1), &SonServerGymEnv::ScheduleNextStateRead, this);
    }

    // SonServerGymEnv::SonServerGymEnv (Time steptime){
    //     NS_LOG_FUNCTION(this);
    //     m_interval = Seconds(steptime);

    //     Simulator::Schedule (Seconds(0.0), &SonServerGymEnv::ScheduleNextStateRead, this);
    // }

    void SonServerGymEnv::ScheduleNextStateRead() {
        NS_LOG_FUNCTION(this);

        Notify();
        Simulator::Schedule (m_interval, &SonServerGymEnv::ScheduleNextStateRead, this);

    }

    SonServerGymEnv::~SonServerGymEnv(){
        NS_LOG_FUNCTION(this);
    }

    TypeId SonServerGymEnv::GetTypeId (void) {
        static TypeId tid = TypeId("SonServerGymEnv")
            .SetParent<OpenGymEnv> ()
            .SetGroupName ("OpenGym")
            .AddConstructor<SonServerGymEnv> ()
            //New Part
            /*
            .AddAttribute("ueNum","Total Number of UE",
                            UintegerValue(0),
                            MakeIntegerAccessor(&SonServerGymEnv::ueNum),
                            MakeUintegerChecker<uint16_t> ())
            */
        ;
        return tid;
    }

    void SonServerGymEnv::DoDispose(){
        NS_LOG_FUNCTION(this);
    }

    void SonServerGymEnv::AddNewNode(uint16_t cellId, Ptr<LteEnbNetDevice> dev){
        
        m_enbs.insert(std::pair<uint32_t, Ptr<LteEnbNetDevice>> (cellId, dev));
    }



    Ptr<OpenGymSpace> SonServerGymEnv::GetObservationSpace(){
        NS_LOG_FUNCTION(this);
        uint32_t nodeNum = m_enbs.size();
        uint32_t carrierNum = 1;
        //New Part, Num + 1
        uint32_t Num = nodeNum * carrierNum;
        std::vector<uint32_t> shape {Num,};

        std::string dtype = TypeNameGet<double> ();

        Ptr<OpenGymBoxSpace> box = CreateObject<OpenGymBoxSpace> (0, 100, shape, dtype);
        
        Ptr<OpenGymDictSpace> space = CreateObject<OpenGymDictSpace> ();
        space->Add("dlPrbUsage",box);
        NS_LOG_INFO("GetObservationSapce: "<<box);

        return space;

    }

    Ptr<OpenGymSpace> SonServerGymEnv::GetActionSpace(){
        uint32_t nodeNum = m_enbs.size();
        std::vector<uint32_t> shape {nodeNum,};

        std::string dtype = TypeNameGet<int32_t> ();

        Ptr<OpenGymBoxSpace> box = CreateObject<OpenGymBoxSpace> (-24, 24, shape, dtype); //todo range change for -30 to 30
        // Ptr<OpenGymBoxSpace> box = CreateObject<OpenGymBoxSpace> (0, 0, shape, dtype); //todo range change for -30 to 30
        Ptr<OpenGymDictSpace> space = CreateObject<OpenGymDictSpace> ();

        space->Add("Offset", box);

        NS_LOG_INFO("GetObservationSapce: "<<box);

        return space;
    }

    bool SonServerGymEnv::GetGameOver(){
        bool isGameOver = false;
        bool test = false;
        static float stepCounter = 0.0;
            if (stepCounter == 100 && test) {
                isGameOver = true;
            }
        stepCounter += 1;
        NS_LOG_UNCOND("Game OVER: "<< isGameOver);
        return isGameOver;
    }

    Ptr<OpenGymDataContainer> SonServerGymEnv::GetObservation(){
        NS_LOG_FUNCTION(this);
        // std::cout<<"GetObservation";
        uint32_t nodeNum = m_enbs.size();
        int32_t carrierNum = 1;
        uint32_t Num = nodeNum * carrierNum;
        std::vector<uint32_t> shape {Num,};

        Ptr<OpenGymBoxContainer<double>> box = CreateObject<OpenGymBoxContainer<double>> (shape); 

        double ueNum;
        for (std::map<uint32_t, Ptr<LteEnbNetDevice>>::iterator iter = m_enbs.begin(); iter != m_enbs.end(); ++iter){
            ueNum += (double)(iter->second->GetRrc ()->m_numofues);
            }

        //Calculate Dl PRB Usage in Son Server
        for (std::map<uint32_t, Ptr<LteEnbNetDevice>>::iterator iter = m_enbs.begin(); iter != m_enbs.end(); ++iter){
            double numofues;
            double dlprbusage;
            numofues = (double)(iter->second->GetRrc ()->m_numofues);
            dlprbusage = (numofues/ueNum)*(double)100;
            dlprbusage = (round(dlprbusage*100))/100;
            box->AddValue(dlprbusage);
            std::cout<<"DLPRBUsage: "<<dlprbusage;
            }
        Ptr<OpenGymDictContainer> data = CreateObject<OpenGymDictContainer> ();
        data->Add("dlPrbUsage",box);
        std::cout<<"Data OpenGym" <<data<<std::endl; 
        return data;
    }

    float SonServerGymEnv::GetReward(){
        NS_LOG_FUNCTION(this);
        float ret = 0.0;
        return ret;        
    }



    std::string SonServerGymEnv::GetExtraInfo() {
        std::string myinfo = "testSON";
        return myinfo;

    }

    bool SonServerGymEnv::ExecuteActions(Ptr<OpenGymDataContainer> action){
        Ptr<OpenGymDictContainer> dict = DynamicCast<OpenGymDictContainer>(action);
        Ptr<OpenGymBoxContainer<int32_t> > box = DynamicCast<OpenGymBoxContainer<int32_t>>(dict->Get("Offset"));

        uint32_t nodeNum = m_enbs.size();
        std::list<LteRrcSap::CellsToAddMod> celllist_temp;
        std::cout<<"ExecuteActions: ";
        for(uint32_t i = 0; i < nodeNum; i++){
            LteRrcSap::CellsToAddMod cell_temp;
            cell_temp.cellIndex = i+1;
            cell_temp.physCellId = 0;
            cell_temp.cellIndividualOffset = box->GetValue(i);
            celllist_temp.push_back(cell_temp);
            std::cout<<box->GetValue(i);
        }
        // std::list<Ptr<LteEnbNetDevice>>::iterator iter;
        // for (iter = m_enbs.begin(); iter != m_enbs.end(); ++iter){

        //     iter->m_rrc->setCellstoAddModList(celllist_temp);
        // }
        for (std::map<uint32_t, Ptr<LteEnbNetDevice>>::iterator iter = m_enbs.begin(); iter != m_enbs.end(); ++iter){
            iter->second->m_rrc->setCellstoAddModList(celllist_temp);
        }
        return true;
    }

}