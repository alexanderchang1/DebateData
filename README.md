# DebateData
Data project for APDA style tab cards

Current working version of a program designed to scrape competitor data out of APDA style tab cards. Takes individual tab cards and separates them into new dataframes for each competitor and exports them as CSVs.


Any file that starts with test - strips the relevant tab cards for that particular python script, each one usually needs to be edited to specific tab cards due to quirks in tabula.

Currently working on additional scripts for processing data once a competitor CSV is imported into a dataframe. 

Also starting to clean code to integrate into a Master driver script to strip a series of tab cards and process competitor tab cards sequentially. 

Also need to update test files to check for existing competitors to avoid duplicating competitor files. 
