import numpy as np
import pandas as pd
import sys
import errno
from tabula import wrapper
import PyPDF4 as pyPdf4
from PyPDF4 import PdfFileWriter, PdfFileReader
import pdfCropMargins as pdfc
import xarray as xr
filelocation = r"C:\Users\super\PyCharmProjects\untitled\gwnov_tabcards.pdf"
reader = pyPdf4.PdfFileReader(open(filelocation,'rb'))
pgnumber = reader.getNumPages()

'''

from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger

pdf_file = PdfFileReader(open(filelocation,"rb"))
page = pdf_file.getPage(0)
print(page.cropBox.getLowerLeft())
print(page.cropBox.getLowerRight())
print(page.cropBox.getUpperLeft())
print(page.cropBox.getUpperRight())

adjustment = 30 

page.mediaBox.lowerLeft = (adjustment, adjustment)
page.mediaBox.lowerRight = (612-adjustment, adjustment)
page.mediaBox.upperLeft = (adjustment, 792-adjustment)
page.mediaBox.upperRight = (612-adjustment, 792 - adjustment)


#for example :- my custom coordinates
#page.mediaBox.lowerRight = (611, 500)
#page.mediaBox.lowerLeft = (0, 500)
#page.mediaBox.upperRight = (611, 700)
#page.mediaBox.upperLeft = (0, 700)



with open(filelocation, "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = input1.getNumPages()
    print("document has %s pages." % numPages)

    for i in range(numPages):
        page = input1.getPage(i)
        print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        #page.trimBox.lowerLeft = (30, 30)
        #page.trimBox.upperRight = (612-30, 792-30)
        page.cropBox.lowerLeft = (30, 30)
        page.cropBox.upperLeft = (30, 792 - 30)
        page.cropBox.upperRight = (612-30, 792-30)
        page.cropBox.lowerRight = (612-30, 30)
        output.addPage(page)

    with open("out.pdf", "wb") as out_f:
        output.write(out_f)

'''

counter = 0;

pd.set_option('display.max_columns', 10)
CompetitorDatabase = pd.DataFrame(columns = ['Name','ID_No'])
team_name_database = pd.DataFrame(columns = ['Team Name', 'Debater 1', 'Debater 2'])

for a in range (0,pgnumber): #pgnumber, change to 2 for testing purposes
    df = wrapper.read_pdf(filelocation, guess = False, pages = a, area = "0,0,0,0", multiple_tables=True)
    print(df)

    for teamnumber in range (0,2):
        #print("teamnumber")
        team = pd.team1= df[teamnumber]
        team1_fixed = team.replace(to_replace = r"\r", value = " ", regex = True)
        #if a == 1 and teamnumber == 1:
        #    print(team1_fixed)
        tab_card_size= team1_fixed.shape
        #if a == 2 and teamnumber == 0:
        #    print(team1_fixed)

        #if a == 2 and teamnumber == 1:
        #print(team1_fixed)


        ######################################################################################################


        debater1 = " "
        debater2 = " "
        i = 2
        j = 3
        while str(team1_fixed.iloc[0,1]) == str(team1_fixed.iloc[0,7]):

            team1_fixed.iloc[0,1] = team1_fixed.iloc[0,i]
            team1_fixed.iloc[0,i] = team1_fixed.iloc[0,7]
            i = i+1
            print(team1_fixed.iloc[0, :])
        while str(team1_fixed.iloc[0,2]) == str(team1_fixed.iloc[0,7]):

            team1_fixed.iloc[0,2] = team1_fixed.iloc[0,j]
            team1_fixed.iloc[0,j] = team1_fixed.iloc[0,7]
            j = j+1
            print(team1_fixed.iloc[0, :])
        #if counter == 5:
            #print(team1_fixed.iloc[0,:])

        ######################################################################################################

        columnIndex = pd.DataFrame(columns = ['Empty Columns'])
        #print(tab_card_size)
        columnDeletionNeeded = False

        #Checks for empty columns and deletes them


        for columns in range (0, tab_card_size[1]):
            columnEmpty = True

            for rows in range (0, tab_card_size[0]):

                #if columns == 5:

                #print(team1_fixed.iloc[rows,columns])
                #print(team1_fixed.iloc[0,7])
                    #rint(str(team1_fixed.iloc[rows,columns]) != str(team1_fixed.iloc[0,7]))
                #print(rows)
                #print(columns)
                #print(team1_fixed.shape)
                #print(rows)
                #print(columns)
                #print(team1_fixed)
                if str(team1_fixed.iloc[rows,columns]) != str(team1_fixed.iloc[0,columns]):
                    columnEmpty = False


            if columnEmpty:
                columnIndex = columnIndex.append(pd.Series([columns], index = columnIndex.columns), ignore_index = True)
                #print(columnIndex)
                columnDeletionNeeded = True

        #print(columnDeletionNeeded)
        if columnDeletionNeeded:
            for deletions in range (0, columnIndex.shape[0]):
                #print("Column Index")
                #print(columnIndex.iloc[deletions,0])
                deletedColumn = columnIndex.iloc[deletions,0]
                #print("deleted column")
                #print(deletedColumn)
                team1_fixed = team1_fixed.drop(deletedColumn,axis = 1)
                tab_card_size = team1_fixed.shape
                #print(team1_fixed)
        tab_card_size = team1_fixed.shape

        ######################################################################################################


        for nameCycle in range (0, tab_card_size[1]):

                if str((team1_fixed.iloc[0, nameCycle])) != str((team1_fixed.iloc[0, 7])):
                    teamName = team1_fixed.iloc[0,0]
                    teamName = str(teamName)[6:]
                    for name1Check in range(1,tab_card_size[1]):
                        if debater1 == " ":
                            if str((team1_fixed.iloc[1, name1Check])) != str((team1_fixed.iloc[0, 7])):
                                #print(name1Check)
                                debater1 = team1_fixed.iloc[0,name1Check]
                                debater1 = str(debater1)[:-3]
                                #print(debater1)

                                for name2Check in range(name1Check+1,tab_card_size[1]):
                                    if debater2 == " ":
                                        if str((team1_fixed.iloc[0, name2Check])) != str((team1_fixed.iloc[0, 7])):
                                            #print(name2Check)
                                            debater2 = team1_fixed.iloc[0,name2Check]
                                            debater2 = str(debater2)[:-3]

                                #print(debater2)
                tmdb_size = team_name_database.shape
                teamNameExists = False
                for search in range (0,tmdb_size[0]):
                    if team_name_database.iloc[search,0] == teamName:
                        teamNameExists = True


                if not teamNameExists:
                    team_name_database = team_name_database.append(pd.Series([teamName,debater1,debater2], index=team_name_database.columns), ignore_index=True)
                    #print(team_name_database)
        #print(team1_fixed)

        ######################################################################################################


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
                        existingCounter = c;
                if not alreadyExists:
                    pd.newCompetitor = name;
                    CompetitorDatabase = CompetitorDatabase.append(pd.Series([name, np.nan], index = CompetitorDatabase.columns), ignore_index=True)
                    #print(CompetitorDatabase)

                    CompetitorDatabase.iloc[-1, 1] = counter
                    newDatafile = pd.DataFrame(columns = ['Tournament', 'Round', 'Gov/Opp','Win/Loss','Opponent','Judge','Partner','Speaks','Ranks'])


                    numberOfRows = team1_fixed.shape[0]
                    numberOfRounds = numberOfRows - 3
                    #print(numberOfRounds)
                    for round in range (0,numberOfRounds+1):

                        newDatafile = newDatafile.append(pd.Series(["GW Novice 2019",np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index = newDatafile.columns), ignore_index = True)
                        newDatafile.iloc[round, 1] = team1_fixed.iloc[round+1,0] #Round
                        newDatafile.iloc[round, 2] = team1_fixed.iloc[round+1, 1] # G/O
                        newDatafile.iloc[round, 3] = team1_fixed.iloc[round+1, 2] # W/L
                        newDatafile.iloc[round, 4] = team1_fixed.iloc[round+1,3] # Opponent
                        newDatafile.iloc[round, 5] = team1_fixed.iloc[round+1,4] # Judge
                        for partnerNumber in range(0, tab_card_size[1]):
                            if str(team1_fixed.iloc[0, partnerNumber]) != str(team1_fixed.iloc[0, 7]):
                                testName = str(team1_fixed.iloc[0,partnerNumber])[:-3]
                                #print(testName)
                                #print(name)
                                #print(str(testName) == str(name))
                                if testName != name:
                                    PartnerName = team1_fixed.iloc[0,partnerNumber]
                                    partnerKey = partnerNumber
                                    #yourNumber = b
                                    #print(PartnerName)
                        newDatafile.iloc[round, 6] = str(PartnerName)[:-3]
                        for namelook in range(0,tab_card_size[1]):
                            ownNameCheck = team1_fixed.iloc[0,namelook]
                            ownNameCheck = str(ownNameCheck)[:-3]
                            if ownNameCheck == name:
                                yourNumber = namelook
                                if yourNumber < partnerKey:
                                    speaks_ranks = team1_fixed.iloc[round + 1, -3]
                                if yourNumber > partnerKey:
                                    speaks_ranks = team1_fixed.iloc[round + 1, -2]
                                if str(speaks_ranks) == str("nan"):
                                    speaks_ranks = " "


                                #print(speaks_ranks)
                                speaks = str(speaks_ranks)[1:5]
                                ranks = str(speaks_ranks)[6:9]
                                newDatafile.iloc[round, 7] = speaks
                                newDatafile.iloc[round, 8] = ranks




                    export_csv = newDatafile.to_csv (r'C:\Users\super\PyCharmProjects\untitled\%s %s.csv'%(counter,name),index = None, header = True)
                    counter = counter + 1

                ######################################################################################################

                #if alreadyExists:

                # Name check ends here once it creates a new person.
                #Add Data to new datafile here.

#Convert to using xarray, for each new person, add an x y panel describing their data, and a z axis name.

#Team name data base
export_csv = team_name_database.to_csv(r'C:\Users\super\PyCharmProjects\untitled\Hopkins_team_names.csv', index=None, header=True)
export_csv = CompetitorDatabase.to_csv(r'C:\Users\super\PyCharmProjects\untitled\CompetitorDatabase.csv', index=None, header=True)



