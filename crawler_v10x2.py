


    


# In[7]:

import pickle
import proxypool
# usage:
# cralwer_v10.py 3        /usr/local/bin/phantomjs 60005            3
#                job號碼   phontomjs執行檔位置        查詢流水號，可接關  proxy_tick

tasknum = sys.argv[1]
path_phantomjs = sys.argv[2]


#tasknum = 1
#path_phantomjs = '/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs'



task_dir = './task_ini/'
task = pickle.load(open(task_dir+'instance-g{}_v10.x2_job.pkl'.format(tasknum), 'rb'))
taskstart = int(sys.argv[3]) if len(sys.argv) >= 4 else int(task[0][0])
#proxy_tick = int(sys.argv[4]) if len(sys.argv) >= 5 else 1

#taskstart = 0
#proxy_tick = 20

#config['TASK']['1']
#task_proxy = proxypool.proxypool(path_phantomjs = path_phantomjs)
#task_proxy.proxy_set_max = 100
#task_proxy.world_proxy()

crawler = cmpyinfo_crawler(path_phantomjs = path_phantomjs, logname='instance{}_v10.x2_job.log'.format(tasknum), sleep_scale='none')
crawler.proxypool.proxy_set_max = 150
crawler.proxypool.group_proxy()
#crawler.proxy_tick = proxy_tick
crawler.proxypool.none_freq = 4

#crawler.qryCond = t[1]
#crawler.qryType = t[2]
#crawler.pageStart = t[3]
#crawler.pageEnd = t[4]

for t in task:

    
    crawler.qryCond = t[1]
    crawler.qryType = t[2]
    crawler.pageStart = t[3]
    crawler.pageEnd = t[4]
    if int(t[0]) < taskstart:
        continue
        
    print("======================================")
    print("task ", t[0], ": ", t[1], "@", t[2])
    print("======================================")
    
    crawler.search_error_cnt = 0
    crawler.set_form_data_url1(mode = 0, currentPage = 1)
    while not crawler.first_connection() and crawler.search_error_cnt < 6:
        crawler.change_proxy()

    if not crawler.search_error_cnt < 6:
        crawler.search_error_cnt = 0
        continue
    crawler.search_error_cnt = 0
    #time.sleep(random.choice([5,5.5,6,7,10,3,5,4,7,7,1]))
    crawler.resolve_page()
    crawler.parse_and_gen_schema(1, crawler.totalPage)
    
    #if crawler.proxy_tick < 0:
    #    import random
    #    time.sleep(random.randint(50,70))
    #else:
    #    crawler.proxy_monitor()


# In[ ]:



