#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  date  2020-11-9
## ahthor : james jia 
 
import requests
import json
import sys
import os
import datetime
import random
import sched 
import time
import xlrd


ERROR_MSG = "暂无错误发现"
ERROR_MSG_type_1 = "矿工不存在或没有work余额显示"
ERROR_MSG_type_2 = "矿工work余额低于阈值"

DINGDING_URL = 'https://oapi.dingtalk.com/robot/send?access_token=ff9cbd63300425e58480691a3b5e47e029be4bd37553f526a93b40c80cea5935'
SHEDULE_CHECK_INTERVAL_TIME =  300     #300秒为一轮矿工信息检查的间隔时间
LOOP_INTERVAL_TIME = 4   #发送钉钉消息的频率为4秒一个，防止过高导致触发钉钉请求并发阈值





#***********每隔 SHEDULE_CHECK_INTERVAL_TIME 秒请求所有矿工的矿工信息*************************************
def  schedule_run_filecoin_post():
     while True:
         global SHEDULE_CHECK_INTERVAL_TIME
         run_filecoin_excel( )
         time.sleep(SHEDULE_CHECK_INTERVAL_TIME)


#****************xls读取矿工对应信息*************************************************
def  run_filecoin_excel( ):
     MinerDatas= xlrd.open_workbook(r'filecoin_msg.xls')
     Sheet1 =  MinerDatas.sheet_by_index(0)
     Rows = Sheet1.nrows
#   Cols = Sheet1.ncols
     global  LOOP_INTERVAL_TIME
     CheckTime = int(int(Rows)*LOOP_INTERVAL_TIME/60+1)
     print("当前时间:"+str(get_cur_time())+" 开启新一轮矿工余额检查，预计耗时"+str(CheckTime)+"分钟")
     for i in range(1,Rows):
         ClusterName = Sheet1.cell(i,0).value
         MinerId = Sheet1.cell(i,1).value
         ThresholdValue = Sheet1.cell(i,2).value
         send_filecoin_post_msg(MinerId,ThresholdValue,ClusterName)
         time.sleep(LOOP_INTERVAL_TIME)
     WaitTime =  int(SHEDULE_CHECK_INTERVAL_TIME/60)+1   
     print("当前时间:"+str(get_cur_time())+" 请等待下一轮检查，预计等待时间"+str(WaitTime)+"分钟")       


#****检查返回字段是否有对应的key****************************************************
def  check_json_key(Datas,TargetKey):
     for key  in   Datas.keys():
         if key == TargetKey:
            return True
     return  False


#************依据矿工ID发送post进行矿工信息请求**********************************************************
def  send_filecoin_post_msg(MinerId,ThresholdValue,ClusterName):
#    filecoin_url = "https://filfox.info/api/v1/address/f023569"
     FilecoinUrl = "https://filfox.info/api/v1/address/"+str(MinerId)
     FilecoinPayload = {}
     FilecoinHeaders= {}
     FilecoinResponse = requests.request("GET",FilecoinUrl, headers=FilecoinHeaders, data=FilecoinPayload)
     FilecoinResponse.encoding = 'uft8'
     FilecoinJson = FilecoinResponse.json()
     WorkBalanceState = check_json_key(FilecoinJson,"miner")
     global   ERROR_MSG
     if   WorkBalanceState:    #开始进行阀值比较
         WorkBalance = int(FilecoinJson['miner']['owner']['balance'])//1000000000000000000
         if  int(WorkBalance) <= int(ThresholdValue):
             ERROR_MSG = ERROR_MSG_type_2
       #     print("当前矿工ID"+str(MinerId)+" 还没到告警阈值")  
             send_dingding_post_msg(MinerId,ClusterName,WorkBalance)
     else:
             ERROR_MSG = ERROR_MSG_type_1
             send_dingding_post_msg(MinerId,ClusterName,0)
     

#****************获取当前时间*************************************************************************
def  get_cur_time():
    #NowTime=datetime.datetime.now().strftime('%Y'+'年'+'%m'+'月'+'%d'+'日'+'%H'+'时'+'%M'+'分'+'%S'+'秒')
     UTCTimeStamp = int(time.time())+8*60*60
     BeijingTime  = datetime.datetime.fromtimestamp(UTCTimeStamp)
     return BeijingTime 


#**************随机筛选出图床中的图片*****************************************************************
def  random_img_url( ):
    RandNum = random.randint(0,4)
    ImgUrls = ['https://ftp.bmp.ovh/imgs/2020/11/8a1474c3c257c37e.png','https://ftp.bmp.ovh/imgs/2020/11/af4b6239595536ed.png','https://ftp.bmp.ovh/imgs/2020/11/634eed15231bfa01.png','https://ftp.bmp.ovh/imgs/2020/11/5a98bcbadbc65a65.png','https://ftp.bmp.ovh/imgs/2020/11/3df411c8ba660202.png']
   #print("random num**"+ ImgUrls[randnum])
    return  ImgUrls[RandNum] 


#************发送psot请求给钉钉机器人**********************************************************************
def  send_dingding_post_msg(MinerId,ClusterName,WorkBalance):
     DingdingHeaders = {'Content-Type': 'application/json;charset=utf-8'}
     ImgUrl = str( random_img_url() )
     CurTime = str( get_cur_time() )
     MarkDownContent = ""
     if  ERROR_MSG ==  ERROR_MSG_type_1:
         MarkDownContent = "# filecoin矿工告警!!!\n>集群名: "+str(ClusterName)+"   矿工ID: "+str(MinerId)+"\n\n>"+ERROR_MSG+"\n\n>"+"#### ![screenshot]("+ImgUrl+")\n>##### "+CurTime+" 发布\n"
     else:
         MarkDownContent = "# filecoin矿工告警!!!\n>集群名: "+str(ClusterName)+"   矿工ID: "+str(MinerId)+"\n\n>余额为"+str(WorkBalance)+"急需补充!!!\n\n>"+"##### ![screenshot]("+ImgUrl+")\n>##### "+CurTime+" 发布\n"

     DingdingHeaders = {
         "Content-Type": "application/json",
         "Chartset": "utf-8"
               } 
     DingdingRequestData = {
          "msgtype": "markdown",
          "markdown": {
               "title":"filecoin告警",
               "text": MarkDownContent
                      },
                       "at": {
                "atMobiles": [
                        "150XXXXXXXXX"
                             ],
               "isAtAll": True
                             }
                }
     DingdingSendData = json.dumps(DingdingRequestData)
     global DINGDING_URL
     DingdingResponse = requests.post(url=DINGDING_URL,headers=DingdingHeaders,data=DingdingSendData).json()
     code = DingdingResponse["errcode"]
     if code == 0:
         print("有告警,钉钉消息发送成功,返回码:" + str(code) + "\n")
     else:
         print("有告警,钉钉消息发送失败,返回码:" + str(code) + "\n")
         exit(3)





#****main函数总入口***************************************************************************88
if __name__ == '__main__':
     schedule_run_filecoin_post()
     get_cur_time()
