## a web scraping project using scrapy.

The targeted site is [classcentral.com](www.classcentral.com)
in which I scraped the whole site for the following data points.
1. course's subject.
2. course's title.
3. course's url

I got 16173 records. [classcentral.com](http://www.classcentral.com) is  listing all the free and partial free online available 
courses offered by different universities and institutes for the various topics and subjects. also ranking them by 
their popularity and content.

### Instruction to execute a project
1. install scrapy.
    > pip install scrapy
2. open CLI and go to the project directory. run this command:
    > scrapy crawl subjects
3. if you want data for a specific subject then:
    > scrapy crawl subject -a subject="programming"
4. if you want to save scrape data in any of format i.e. CSV, XML, and 
JSON then used this command.
    > scrapy crawl subject -o data.csv <br/> 
    scrapy crawl subject -o data.json

