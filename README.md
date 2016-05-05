# 150_final

This is a work in progress. 

This work contains scripts to trace Telegram's data center, their latencies,  and attempts to measure the time it takes to send each message 

-So far, I can measure the time using a wrapper around a CLI implementation of the Telegram client.  

-I am on the way to implementing a stand alone client based on Telepy's module. 
-Main challenge has been working around their MTproto authentication scheme and working around their RPC based API calls. 
-Most of the work has involved reverse engineering existing client's listed below: 

https://github.com/vysheng/tg
https://github.com/luckydonald/pytg
https://github.com/griganton/telepy
https://github.com/zhukov/webogram
