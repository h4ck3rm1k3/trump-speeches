from bs4 import BeautifulSoup
f=open ('Search _ C-SPAN.orgTrump.html')
html_doc=''
for x in f:
    html_doc = html_doc + x
    
soup = BeautifulSoup(html_doc, 'html.parser')
#print soup

li = soup.find_all('li')
talks =[]

for x in li:
    video = datetime = 'none'
    if x.has_attr('class'):
        c = x['class'][0]
        if c != 'onevid':
            continue
        
        # time attrib
        time = x.find_all('time')
        for t in time:
            datetime = t['datetime']

        # video
        vids = x.find_all('a')
        for v in vids:
            #print v
            if v['class'][0] == 'thumb' :
                video = v['href']
                # find the h3
            for h3 in v.find_all('h3'):
                title=h3.text

        #time datetime
        
            #print(p.encode('utf-8'))
        talks.append({'title': title, 'video': video, 'datetime':datetime})
        
#class="onevid">
import json
print json.dumps(talks,indent=4, sort_keys=True)
