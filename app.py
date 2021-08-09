from datetime import datetime, timedelta
from typing import List,Dict

class Campaign:
    def __init__(self, id, campaignname, date1, date2):
        self.name = campaignname
        self.startdate  = datetime.strptime(date1,"%m/%d/%Y")
        self.enddate = datetime.strptime(date2,"%m/%d/%Y")
        

campaign1 =Campaign(1,"campaign1", "01/01/2021", "01/05/2021")
campaign2 =Campaign(2,"campaign2","01/10/2021","01/15/2021")
campaign3 =Campaign(3,"campaign3", "01/20/2021", "01/25/2021")

campaign_list=[]

def datetime_range(start=None, end=None):
    span = end - start
    print(span)
    for i in range(span.days):
        a= start + timedelta(days=i)
        yield a

def findgaps(start=None, end=None) -> List:
    missingdatelist =[]
    for date in datetime_range(start=start, end=end):         
            print(date)
    return missingdatelist

def schedule_campaigns(campaing: Dict)-> List:
    global campaign_list
    campaign_list.append(campaing)
    return campaign_list    
        

b =schedule_campaigns(campaign1.__dict__)
c =schedule_campaigns(campaign2.__dict__)
print([x for x in campaign_list])
print(findgaps(campaign1.enddate,campaign2.startdate))

