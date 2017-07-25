# ProdirectScraper

## Instalation

Installing Scrapy inside a virtual environment on all platforms.

Python packages can be installed either globally (a.k.a system wide), or in user-space. We do not recommend installing scrapy system wide.

Instead, we recommend that you install scrapy within a so-called “virtual environment” (virtualenv).

Virtualenvs allow you to not conflict with already-installed Python system packages (which could break some of your system tools and scripts), and still install packages normally with pip (without sudo and the likes).

To install it globally (having it globally installed actually helps here), it should be a matter of running:

```
$ [sudo] pip install virtualenv
```

Inside virtual env install ProdirectScraper dependencies:

```
pip install -r requirements.txt
```

## Config Settings

These are the required configuration options :
```
#avaiable size are from 4 to 12, e.g 4 or 4,5,10
size =
# avaiable currency EUR,USD,GBP
currency = 
smtp_host =
mail_from =
mail_to = 
smtp_user =
smtp_pass =
smtp_port =
smtp_tls =
smtp_ssl =

```

