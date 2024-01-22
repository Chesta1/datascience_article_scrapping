from scrapers.scraping_script import scraping_titles
from drivers.setting_driver import SetupDriver

import pandas as pd 
import json
# from .drivers.setting_driver import SetupDriver

class data_towards_datascience:
    def __init__(self):
        self.url = "https://towardsdatascience.com/latest"
        self.towards_ds_xpath_title = "//*[contains(@class,'graf') and contains(@class,'graf--h3') and contains(@class,'graf--title')]"
        self.towards_ds_xpath_date = "//time[@datetime]"
        self.towards_ds_xpath_subtitle= "//*[@class='graf graf--h4 graf-after--h3 graf--trailing graf--subtitle']"

    def get_data(self,driver_path):
        
       
        data = scraping_titles.scrape_articles(driver_path,self.url,self.towards_ds_xpath_title,self.towards_ds_xpath_subtitle,self.towards_ds_xpath_date,scraping_titles.parse_towards_ds_date,days_back=30, scroll_pause_time=30)

        towards_df =pd.DataFrame(data,columns=None)
        towards_df['date'] = pd.to_datetime(towards_df['date'])

        return towards_df
        

class data_science_central:
    def __init__(self):
        self.data_science_central_url = "https://www.datasciencecentral.com/articles/"
        self.data_science_central_xpath_title = "//*[contains(@class,'blog-entry-title entry-title')]/a[@rel='bookmark']"
        self.data_science_central_xpath_date = "//*[contains(@class,'entry-date published')]"
        self.data_science_central_xpath_subtitle="//*[@class='excerpt-wrap entry-summary']"

    def get_data(self,driver_path):
        
       
        data = scraping_titles.scrape_articles(driver_path,self.data_science_central_url,self.data_science_central_xpath_title,self.data_science_central_xpath_subtitle,self.data_science_central_xpath_date,scraping_titles.parse_data_science_central_date,days_back=30, scroll_pause_time=30)

        dsc_df =pd.DataFrame(data,columns=None)
        dsc_df['date'] = pd.to_datetime(dsc_df['date'])

        return dsc_df
    
class level_up:
    def __init__(self):
        self.levelup_url = "https://levelup.gitconnected.com/latest"
        self.levelup_xpath_title = "//*[contains(@class, 'graf') and contains(@class, 'graf--h3') and contains(@class, 'graf-after--figure') and contains(@class, 'graf--trailing') and contains(@class, 'graf--title')]"
        self.levelup_xpath_date = "//time[@datetime]"
        self.levelup_xpath_subtitle= "//*[contains(@class, 'graf') and contains(@class, 'graf--h4') and contains(@class, 'graf-after--h3') and contains(@class, 'graf--trailing') and contains(@class, 'graf--subtitle')]"
    def get_data(self,driver_path):
        
       
        data = scraping_titles.scrape_articles(driver_path,self.levelup_url,self.levelup_xpath_title,self.levelup_xpath_subtitle,self.levelup_xpath_date,scraping_titles.parse_towards_ds_date,days_back=30, scroll_pause_time=30)

        level_up_df =pd.DataFrame(data,columns=None)
        level_up_df['date'] = pd.to_datetime(level_up_df['date'])

        return level_up_df

        
