There are cspan videos with transcripts :
https://www.c-span.org/video/?418090-1/donald-trump-elected-45th-president-united-states

First I ran a search by person and scrolled to the end, saving the results to html, these search results are used to produce an index.

https://www.c-span.org/person/?donaldtrump

then you save the results to a file 'Search _ C-SPAN.orgTrump.html' and run
parse_cspan_curl.py parses the results of that and produces a bash curl script to download all the transcripts.

Note, the actual texts are copyrighted by the federal news service. 

You will find the index in talks.json, example :

    {
        "datetime": "2016-12-28", 
        "prog_id": "465208", 
        "title": "President-Elect Trump and Don King News Conference", 
        "video": "https://www.c-span.org/video/?420868-2/presidentelect-trump-don-king-news-conference"
    }, 

Now, after you generate the curl script and download all the transcripts, you run the second script that parses them and produces the transcript json files,
they are per talk and look like this :

     python parse_cspan_transcript.py
	 
The output looks like this :

	{
    "datetime": "2015-08-16", 
    "filename": "410937Donald_Trump_on_Third_Parties.html", 
    "prog_id": "410937", 
    "text": [
        {
            "speaker": "Unidentified Speaker", 
            "text": " I GET WHAT YOU DON'T WANT TO RUN\nAS AN INDEPENDENT.", 
            "timecode": "\n00:00:05\n"
        }, 
        {
            "speaker": "TRUMP", 
            "text": " I AM NOT PREPARED TO CLOSE A\nDOOR YET. I WOULD NOT BE SURPRISED IF\nSOMEDAY IN THE FUTURE IT HAPPENS.\nTHEY TREATED ME VERY WELL. I\nJUST WANTED", 
            "timecode": "\n00:00:05\n"
        }
		...
	]
	}
	
	
Note, the script dont read the json yet so you will need to save the search yourself or adjust the code.
