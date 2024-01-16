from datetime import date, timedelta
import requests
import time

today = date.today()

api_list= ["VoltageFileInsert","LinesFileInsert","MVARFileInsert","ICTFileInsert","FrequencyFileInsert","DemandFileInsert","GeneratorFileInsert","ISGSFileInsert"]

for i in range(1,8):
    
    endDate = startDate = str(today - timedelta(days=i))

    for api in api_list:

        api_link = "http://10.3.200.63:5010/"+api+"?startDate=" + \
            startDate+"&endDate="+endDate
        
        f = requests.get(api_link)
        time.sleep(10)
        print(api_link,"\n",f.text)
        time.sleep(1)

