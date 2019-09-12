aimport numpy as np
import pandas as pd
import sys
import errno
from tabula import read_pdf
import PyPDF4 as pyPdf
import xarray as xr
reader = pyPdf.PdfFileReader(open("Nationals_Tab_Cards.pdf",'rb'))
pgnumber = reader.getNumPages()



pd.set_option('display.max_columns', 10)
CompetitorDatabase = pd.DataFrame(columns = ['Name','File'])

for a in range (0,pgnumber): #pgnumber
    df = read_pdf("Nationals_Tab_Cards.pdf", guess = False, pages = a, area = "34.043,300,38.866", multiple_tables=True)


    for teamnumber in range (0,2):
        #print("teamnumber")
        team = pd.team1= df[teamnumber]

        team1_fixed = team.replace(to_replace = r"\r", value = " ", regex = True)
        #tabcards = xr.DataArray(team1_fixed)
        tab_card_size= team1_fixed.shape
        #print(team1_fixed)
        for b in range (1,tab_card_size[1]):
            if team1_fixed.iloc[0,b] is not team1_fixed.iloc[0,7]:
                name = team1_fixed.iloc[0,b]

                #print(name)
                #print(team1_fixed.iloc[0,b])
                #print(b)
                if isinstance(name,str):
                    name = name[:-3]
                #print(name)
                alreadyExists = False
                nameCheck = name
                # This part checks if the competitor already exists in the database
                for c in range (0,CompetitorDatabase.shape[0]):
                    if nameCheck == CompetitorDatabase.iloc[c,0]:
                        alreadyExists = True
                if not alreadyExists:
                    pd.newCompetitor = name;
                    CompetitorDatabase = CompetitorDatabase.append(pd.Series([name, np.nan], index = CompetitorDatabase.columns), ignore_index=True)
                    #print(CompetitorDatabase)
                    CompetitorDatabase.iloc[-1, 1] = pd.DataFrame(columns=['Tournament','Round','Judge','Partner','Side','Win/Loss','Speaks','Ranks'])
                # Name check ends here once it creates a new person.
                #Add Data to new datafile here.

#Convert to using xarray, for each new person, add an x y panel describing their data, and a z axis name.

print(CompetitorDatabase)


#tabcards = xr.DataArray()



