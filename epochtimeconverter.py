import time
epoch_times = [1586395460, 1586395820,1586396181]

timezone = "IST" #  GMT

if timezone == "IST":
    for timeselected in epoch_times:
        print str(timeselected) + ":" +time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timeselected) )

else:
    for timeselected in epoch_times:
        print str(timeselected) + ":" +time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timeselected) )



