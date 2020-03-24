# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class SubjectsSpider(Spider):
    name = 'subjects'
    allowed_domains = ['classcentral.com']
    start_urls = ['http://www.classcentral.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            subject_url = response.xpath("//*[contains(@title, '" + self.subject.title() + "')]/@href").extract_first()
            yield Request(response.urljoin(subject_url), callback=self.parse_subject)

        else:
            self.logger.info("Scraping all subjects")
            subjects = response.xpath(
                "//*[contains(@class, 'border-box align-middle color-charcoal hover-no-underline')]/@href").extract()

            for subject in subjects:
                abs_path = response.urljoin(subject)
                yield Request(abs_path, callback=self.parse_subject)

    def parse_subject(self, response):

        subject_name = response.xpath('//h1/text()')[0].extract()
        courses = response.xpath('//tr/td/a[@data-track-click="listing_click"]')
        for course in courses:
            course_url = 'https://www.classcentral.com' + course.xpath('.//@href').extract_first()
            course_title = course.xpath('.//span/text()').extract_first().strip()

            yield {'subject_name': subject_name,
                   'course_title': course_title,
                   'course_url': course_url
                   }

            next_page = response.xpath('//link[@rel="next"]/@href').extract_first()
            abs_next_page = response.urljoin(next_page)
            yield Request(abs_next_page, callback=self.parse_subject)
