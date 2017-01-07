from bs4 import BeautifulSoup
import os.path
f=open ('Search _ C-SPAN.orgTrump.html')
html_doc=''
for x in f:
    html_doc = html_doc + x
    
soup = BeautifulSoup(html_doc, 'html.parser')
#print soup

li = soup.find_all('li')
talks =[]

for x in li:
    prog = video = datetime = 'none'
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

        for s in x.find_all('span'):
            c = s['class'][0]
            #print c
            if c=='excerpt':
                prog = s['id'].replace('cc','')
                # get the transcript:
                #<span class="excerpt toLoad" id="cc463252">
               
        
            #print(p.encode('utf-8'))
        #talks.append({'title': title, 'video': video, 'datetime':datetime, 'prog_id': prog })
        filename=prog+title.replace(" ","_").replace("'","_")
        if not os.path.isfile(filename) :
            print """if [ ! -f {filename} ]; then curl '{video}&action=getTranscript&transcriptType=cc&service-url=%2Fcommon%2Fservices%2FprogramSpeakers.php&progid={prog}&appearance-filter=&personSkip=0&ccSkip=0&transcriptSpeaker=&transcriptQuery=' -H 'pragma: no-cache' -H 'accept-encoding: gzip, deflate, sdch, br' -H 'x-requested-with: XMLHttpRequest' -H 'accept-language: en-US,en;q=0.8' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36' -H 'accept: */*' -H 'cache-control: no-cache' -H 'authority: www.c-span.org' -H 'cookie: cspanvl_cc_font=inherit; cspanvl_cc_size=12; cspanvl_cc_foreopacity=1.0; cspanvl_cc_backopacity=1.0' -H 'referer: {video}' --compressed -o {filename}.html; fi """.format(           video=video,            prog=prog,            filename=filename)
            pass
        else:
            print "OK",filename
        
#class="onevid">
#import json
#print json.dumps(talks,indent=4, sort_keys=True)
