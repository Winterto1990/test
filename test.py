#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys    #jest a test
import re
import json
def recursive_json_loads(data):
    if isinstance(data, list):
        return [recursive_json_loads(i) for i in data]
    elif isinstance(data, tuple):
        return tuple([recursive_json_loads(i) for i in data])
    elif isinstance(data, dict):
        return Storage({recursive_json_loads(k): recursive_json_loads(data[k]) for k in data.keys()})
    else:
        try:
            obj = json.loads(data)
            if obj == data:
                return data
        except:
            return data
        return recursive_json_loads(obj)
class Storage(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __repr__(self):
        return dict.__repr__(self)
s = '''2017-02-19 16:20:04	10.77.16.222	10.77.6.230	124	/feed/ml_feed.json	134217728	0
{"expotime":"1487492404","isPageUp":"1","retfid":"1","source":"134217728","uid":"1813577422"}
[{"fidsvals":{"fu_week_ia_interval_equal":"0.0","fuu_affinity":"0.5436","fuu_ia_degree_month":"0.02","fuu_ia_num_month":"2",
   "fuu_ia_num_week":"0","fuu_iar_month":"0.03","fuu_is_fansboth":"0","m_ad":"0","m_chour":"16","m_cmt_degree":"0.002","m_cmt_num_his":"0","m_cmt_num_hour":"0",
   "m_cmt_rate_100":"0.01","m_feed_expo_num_his":"0","m_feed_expo_num_hour":"10","m_fwd_degree":"0.001","m_fwd_num_his":"0","m_fwd_num_hour":"0","m_fwd_rate_100":"0.01","m_has_card":"0",
   "m_has_card_num":"0","m_has_face":"0","m_has_gif":"0","m_has_link":"0","m_has_long_blog_num":"0","m_has_long_pic":"0","m_has_long_pic_num":"0","m_has_music":"0",
   "m_has_pic":"1","m_has_pic_num":"1","m_has_topic":"0","m_has_video":"0","m_has_video_inner":"0","m_has_video_miaopai":"0","m_has_video_miaopai_num":"0",
   "m_has_video_num":"0","m_ia_rate_10":"0.1","m_ia_rate_100":"0.01","m_ia_rate_1000":"0.001","m_is_business":"0","m_is_comment":"0","m_is_first_tblog_day":"1",
   "m_is_inner_service":"0","m_is_long_blog":"0","m_is_original":"1","m_is_toutiao":"0","m_is_transmit":"0","m_lk_degree":"4.0E-4","m_lk_num_his":"0","m_lk_num_hour":"0",
   "m_lk_rate_100":"0.01","m_sourceid":"780","m_u_clevel":"1","m_u_cmt_num_month_fa":"19237","m_u_expo_num_month_fa":"73949661","m_u_filtered_attens_num":"614",
   "m_u_filtered_fans_num":"5911383","m_u_fwd_num_month_fa":"19881","m_u_gender":"1","m_u_ia_num_month_fa":"81519","m_u_lk_degree_opp_month":"1.0","m_u_lk_num_month_fa":"42401",
   "m_u_lkr_opp_month":"5.733892770796109E-4","m_u_tweets_num":"61747","m_u_type":"2","m_u_vtype":"2","mc_time_interval":"0"},"mid":4076900970910283,"modelweight":0.004699999999999704,"timeweight":5.245,"uid":2181597154,"weight":5.2497},
 {"fidsvals":{"fu_week_ia_interval_equal":"0.0","fuu_affinity":"0.0516","fuu_ia_degree_month":"0.0","fuu_ia_num_month":"0","fuu_ia_num_week":"0","fuu_iar_month":"0.01","fuu_is_fansboth":"0","m_ad":"0","m_chour":"16","m_cmt_degree":"0.014","m_cmt_num_his":"6","m_cmt_num_hour":"6","m_cmt_rate_100":"0.012681159420289856","m_feed_expo_num_his":"452","m_feed_expo_num_hour":"568","m_fwd_degree":"0.001","m_fwd_num_his":"0","m_fwd_num_hour":"0","m_fwd_rate_100":"0.0018115942028985507","m_has_card":"0","m_has_card_num":"0","m_has_face":"0","m_has_gif":"0","m_has_link":"0","m_has_long_blog_num":"0","m_has_long_pic":"0","m_has_long_pic_num":"0","m_has_music":"0","m_has_pic":"1","m_has_pic_num":"1","m_has_topic":"0","m_has_video":"0","m_has_video_inner":"0","m_has_video_miaopai":"0","m_has_video_miaopai_num":"0","m_has_video_num":"0","m_ia_rate_10":"0.017316017316017316","m_ia_rate_100":"0.014492753623188406","m_ia_rate_1000":"0.005509641873278237","m_is_business":"0","m_is_comment":"0","m_is_first_tblog_day":"1","m_is_inner_service":"0","m_is_long_blog":"0","m_is_original":"1","m_is_toutiao":"0","m_is_transmit":"0","m_lk_degree":"8.0E-4","m_lk_num_his":"1","m_lk_num_hour":"1","m_lk_rate_100":"0.0036231884057971015","m_sourceid":"873976","m_u_clevel":"2","m_u_cmt_num_month_fa":"2175","m_u_expo_num_month_fa":"1688765","m_u_filtered_attens_num":"712","m_u_filtered_fans_num":"21441","m_u_fwd_num_month_fa":"1723","m_u_gender":"1","m_u_ia_num_month_fa":"5516","m_u_lk_degree_opp_month":"0.1618","m_u_lk_num_month_fa":"1618","m_u_lkr_opp_month":"9.586319806497263E-4","m_u_tweets_num":"22672","m_u_type":"1","m_u_vtype":"0",
       "mc_time_interval":"5"},"mid":4076899518887318,"modelweight":0.004999999999999893,"timeweight":5.202,"uid":1846569133,"weight":5.207}]'''
com = re.compile(r'\[(\{.+\})\]',re.S)
result = com.search(s)
datapro = json.dumps(result.group(0))
data = recursive_json_loads(datapro)
lenths = len(data)
for i in range(lenths-1):
    t1 = data[i]['fidsvals']['mc_time_interval']
    t2 = data[i+1]['fidsvals']['mc_time_interval']
    if t1 < t2:
        print str(data[i]) + "+++" + str(data[i+1])
# print data[0]['fidsvals']['m_u_type']