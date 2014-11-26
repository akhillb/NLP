NLP
===
This repo contains all the files for the NLP project.

24 hours data:
Unique queries: 66566
Unique users: 62696
Unique Click through urls: 24360

48 hours data:
Unique queries: 123930
Unique users: 108007
Unique Click through urls: 42594

72 hours data:
Unique queries: 172482
Unique users: 141343
Unique Click through urls: 57367


data/ - Contains all the files with data
-> data/24hours.txt : Contains search data on March 1,2006
-> data/48hours.txt : Contains search data between March 1,2006 - March 2,2006
-> data/72hours.txt : Contains search data between March 1,2006 - March 3,2006
collect.py - Reads all the initial AOL search log and collects data for 72 hours of search queries
details.py - Reads all the search log and returns statistics like number of users, number of queries and number of click through urls
mine.py - Mines the whole search log and generates the following files
            -> mappings.txt : Contains two dicts containing the mappings of query to urls and url to queries
            -> graph.txt : Contains the adjacency matrix between queries and urls
            -> query.txt : Contains queries and their indices in the search log used for the graph
            -> url.txt : Contains urls and their indices used for the graph

NOTE:
Do not COMMIT mappings.txt, graph.txt, query.txt, url.txt to the repository, as their combined size would be more than 1 GB.
