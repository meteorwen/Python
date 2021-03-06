#!/usr/bin/python
# -*- coding: utf-8 -*-

""""""
""" 爬取学校机构配置 """
wos_organization = "Tsinghua University"

""" mysql配置 """
#dev
#mysql_config = {'host':'localhost','port':3306,'user':'root','passwd':'123456','db':'xjd_crawler','charset':'utf8'}
# pro
mysql_config = {'host':'10.49.10.11','port':3306,'user':'root','passwd':'SUN@xjtu2018','db':'subject','charset':'utf8'}

""" redis数据源配置 """
# dev
#redis_config = {'host':'localhost','port':6379,'decode_responses':True}
# pro
redis_config = {'host':'10.49.10.14','port':6379,'decode_responses':'True'}

""" kafka配置 """
# dev
#kafka_bootstrap_servers = ['192.168.1.130:9092', '192.168.1.130:9093', '192.168.1.130:9094']
# pro
kafka_bootstrap_servers = ['202.117.17.66:9092', '202.117.17.67:9092', '202.117.17.68:9092']

# kafka topic name
kafka_topic = 'wos-qinghdx-list-1'
# kafka consumer config
kafka_consumer_config = {'partition':0,'group_id':'g5'}

"""
    论文爬取范围年份：
        1、爬取所有：startYear=1900，endYear=2018(当前年份)
        2、爬取近10年：startYear=2009，endYear=2018(当前年份)
"""
startYear = "1800"
endYear = "2009"

redis_list_name = "crawler_wos_qinghdx_"
