## Python Course for Code Louisville Summer 2022

### I originally was going to make my project a server dashboard page to connect to my local servers as well as my VPS servers.
### Due to the fact that I got a new job as a Systems Administrator and Application Developer, it took a lot of time away from my work this cohort.
### To make my life easier, I went ahead and switched gears and decided to make a web scraping project because I am already familiar with web scraping with Python before taking this class. I have made a few scrapers already notifying me of a product going below a certain price point on Amazon and sending me an email with the link to the product and the new price.
### To take it a step further, I wanted to scrape data from a website that would have a real world application for me. I have done some projects on the side for clients and one of my clients is a real estate agent and he has requested updated information on listings so that he can use them for his business.

### For this project, I created a Google Colab Notebook which is included in the repo. I also started a self-hosted Jupyter Notebook on one of my VPS servers just to have some variety and to learn about using Jupyter notebooks. One thing I struggled with is reading the database from a remote connection. Hosting the postgres database on my Google Colab Notebook did not seem to work like I wanted. There isn't an easy way for me to make a query on the database using the notebook I was working on to make life simple. I tried to use a Jupyter Notebook on my VPS server as I have complete control over that server. While I can connect to the DB remotely after configuring PostgreSQL correctly to accept incoming connections, I could not get the SSL settings to work in a timely fashion and since class is already over and I am allowed to turn my project in late, this will just be a feature that I cannot completely demonstrate properly.

### To open the Jupyter Notebook on my VPS, please visit the link below and open the Real Estate Scrape.ipynb file. The sections of code can be ran from this site as well as the Google Colab Notebook.
### [Jupyter Notebook hosted at bryanwills.xyz](http://bryanwills.xyz:8888/?token=f82f60f96cd0d1ee39ad8e05592d8b998509d53189ba413a)

### Direct link to [Google Colab Notebook](https://colab.research.google.com/github/bryanwills/python_codelou/blob/main/real_estate_property_info.ipynb#scrollTo=PCM2vtEhKz7e)

### The Google Colab opened up may have a different filename in Google Colab, I was going to do a stock price predcition project and changed the name in Google Drive and Github but for some reason it will still show the stock price name every now and then. The Notebook still runs as intended on Google.

### The 600 response from running this cell from what I have found through research means that all 600 data points were entered into the database ![](https://github.com/bryanwills/python_codelou/blob/main/jupyter_notebook_db_output_success.png)

### Requirements met for this project
- Make a list, dictionary, etc. A list was made to contain the information of the scraped data
- Read in data from a local csv, excel file, json or any other file type. I read in data from a json hosted on a website to get the data points for my project.
- Scrape one piece of data from anywhere on the internet and utilize it in my project. Well I scraped 600 pieces of data and each piece had 7 properties with it so I guess that is 4,200 data points? :)
- Use an API to pull in data. I utilized the built-in API on the website I scraped to get the information by making a curl request with the selected headers.
- Use SQL alchemy. I used it in my project and wrote data to it by confirmation from the Google Colab notebook and the Jupyter Notebook and wrote the 600 data points to it.
- Use pandas to remove null values. I removed datapoints that did not have a value in it by appending an empty string '' for these values.
- I think that is enough to pass! At least I hope so :)

### If you clone this project with the following commands, you can run the project and it will download the .xlsx file to your computer.
### ```git clone https://github.com/bryanwills/python_codelou```
### ```pip3 install -r requirements.txt```
### ```python3 realestate.py```

### Or run one of the notebooks. I made this project compatible in various ways of executing it.

### Note!!! If at any point, running the code ```result_items[0]['Building']['Bedrooms']``` for example and you receive an error saying 'KeyError: 'Bedrooms' an invalid datapoint from the site is reported back. But this is only for one item and is fixed later when appending the data and going through the iterations of the pages. This is code is just showing what happens when trying to search a single listing and is not representing the entire project. Running it again later when another listing shows up, will fix this.