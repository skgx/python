import requests
from bs4 import BeautifulSoup
  
start_URL = "https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start=1000&ref_=adv_nxt"
r = requests.get(start_URL)
#for i in range(1000,8000):



soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
all_h3=soup.find_all("h3");
all_1=[]
for txt in all_h3:
    temp=txt.a
    length=len(temp)
    alll=slice(0,(length-3))
    all_1.append(temp[alll])

for tt in all_1:
    print(tt)
    


