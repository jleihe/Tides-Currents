Created: Wed May 18 21:27:55 PDT 2016
# Written By: Joshua Leihe
# Filename: function.py

import untangle
import datetime

obj = untangle.parse('Data/Tides/GoldenGateBridge.xml')
data = obj.datainfo.data
item = data.item


#Returns the tide on a given day and time
def tide(date, time):
	for i in item:
		date_parts = {}
		d = i.date.cdata
		d = d.split('/')
		
    		item_date = datetime.date(int(d[0]), int(d[1]), int(d[2]))
    		time = i.time.cdata
    		h_l = i.highlow.cdata
		pred = i.predictions_in_ft.cdata
    		
		if item_date == date:
			print time + " -- " +pred + " " + h_l
