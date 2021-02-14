
#LMS Crawler
How to attend classes?!

#Usage
1.Rename ```info.sample.txt``` to the 
```info.txt``` and then modify its content based on your
curriculum, like the sample.

2.Execute below to generate cron jobs:
```
~ python cron_job_generator.py
```

3.Copy generated content in ```cron.txt```.

4.Use below code in Linux OS:
```
~ crontab -e
```
Past the copied content and save the file.

