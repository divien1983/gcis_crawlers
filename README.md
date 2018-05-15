# findbiz

### How to use 
#### script:
以./task_ini的job檔案為例，執行的方式如下  
python crawler_v10x2.py job_name phamtomjs_path subtask  

參數說明：
job_name：當初預計開6台雲端機器，每台同時要跑2個job，所以將job分成n跟n.x, script會再將job_name文字處理成./task_ini內的job檔名
phantomjs_path：phantomjs安裝後執行檔路徑  
subtask：由於一個job可能有上萬筆搜尋，每一筆搜尋給予一個流水號subtask，如此當job發生中斷，可以填入接下來想要的起始subtask接續執行  

範例：  
python crawler_v10x2.py 1 /usr/local/bin/phantomjs 0  
python crawler_v10x2.py 1.x /usr/local/bin/phantomjs 052041  
python crawler_v10x2.py 2 /usr/local/bin/phantomjs 104081  
python crawler_v10x2.py 2.x /usr/local/bin/phantomjs 156121  
python crawler_v10x2.py 3 /usr/local/bin/phantomjs 208161  
python crawler_v10x2.py 3.x /usr/local/bin/phantomjs 260201  
python crawler_v10x2.py 4 /usr/local/bin/phantomjs 312241  
python crawler_v10x2.py 4.x /usr/local/bin/phantomjs 364281  
python crawler_v10x2.py 5 /usr/local/bin/phantomjs 416321   
python crawler_v10x2.py 5.x /usr/local/bin/phantomjs 468361  
python crawler_v10x2.py 6 /usr/local/bin/phantomjs 520401  
python crawler_v10x2.py 6.x /usr/local/bin/phantomjs 572441  


以自訂的關鍵字搜尋為例，執行的方式如下  
python crawler_v11.py phamtomjs_path  
由於所有的job都在script中了，所以直接執行即可，若要切不同的job可以複製多個script，個但每個script給予不同的關鍵字  

參數說明：  
phantomjs_path：phantomjs安裝後執行檔路徑  

範例：  
python crawler_v11.py /usr/local/bin/phantomjs  

### environment
python 3.6  
anaconda 5.0  

### packages
selenium       3.4.3  
requests       2.11.1/2.13.0  
urllib3        1.21.1  
lxml           3.6.4  
fake-useragent 0.1.7  
beautifulsoup4 4.5.1  

https://www.youtube.com/watch?v=kWTDPmSXoyc&feature=youtu.be
