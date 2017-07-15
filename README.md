# SQLgrabbag
Using SQLAlchemy in Python to automate screenscraping (of Financial data) all the way to putting the data into a SQL database

## Summary

I wanted to demonstrate my mastery over SQL and relational databases in general (for job-seeking purposes) and so I pulled up some old, independent passion projects I did way before there was g

### Table of Contents
================

| filename | Description | libraries used |
| -------- | ----------- | -------------- |
| [`./firms_by_NASDAQ.py`](https://github.com/ernestyalumni/SQLgrabbag/blob/master/firms_by_NASDAQ.py) | Initiates the local PostgreSQL database, webscrapes the NASDAQ website for (stock, equity) market data, save that raw data into a `.csv` file, and then saves `.csv` data into SQL database | `requests`, `csv`, `sqlalchemy` |   
| [`./apres_firms_by_NASDAQ.py`](https://github.com/ernestyalumni/SQLgrabbag/blob/master/apres_firms_by_NASDAQ.py) | This is an explicit example of how to use this database of NASDAQ market data, looking up a company, once created by `./firms_by_NASDAQ.py` | `./firms_by_NASDAQ.py`, `sqlalchemy` |
| [`./CUSIP/toSQL.py`](https://github.com/ernestyalumni/SQLgrabbag/blob/master/CUSIP/toSQL.py) | features Python function `build1tomany` which builds a one-to-many relationship between Parent and a Child, which is what SQL relational databases does best; also puts entries ("Rows") into this SQL database | `sqlalchemy` |
| [`./CUSIP/NYSE.py`](https://github.com/ernestyalumni/SQLgrabbag/blob/master/CUSIP/NYSE.py) | As an application of `./CUSIP/toSQL.py`, this creates a SQL database that mimics the ICB Industry Classification Benchmark for companies/firms, giving an industry-wide agreed upon standard for classifying a company into Industry, Sector, etc. for the NYSE | [`./CUSIP/toSQL.py`](https://github.com/ernestyalumni/SQLgrabbag/blob/master/CUSIP/toSQL.py) |

### Tips on running a local PostgreSQL database

Installing and getting a local PostgreSQL database up and running, as an open-source alternative, is non-trivial.  I shared my install process and advice in this blog post:  

[Installing PostgreSQL on a Mac (Mac OS X) tutorial, Introduction on How to run create and run a PostgreSQL database, etc.](https://wordpress.com/stats/post/98/ernestyalumni.wordpress.com)
