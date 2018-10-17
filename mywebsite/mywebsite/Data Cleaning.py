import pandas as pd
from datetime import datetime



#reads the first sheet
df = pd.read_csv("DataInStore.csv", engine = 'python')
df = pd.read_csv("DataInStore.csv", header = None)
df.fillna(value="N/A", inplace = True)

#cleans the file
df[1].replace('Alexandria_stroe', 'Alexandria_store', inplace = True)
df[19].replace(['9-Mar','9-May'], 'Unknown', inplace = True)
df[13].replace(['15, avenue de la Gare','268, avenue de l?Europe','Ro?str 5538','Rotth?user Weg 636','88, avenue de l? Union Centrale'], 'Not Provided', inplace = True)


df.to_csv("CleanedDatainStore.csv", index = False, header = None)

  

#reads the second sheet
cf = pd.read_csv("DataInCentralDatabase.csv", engine = 'python')
cf = pd.read_csv("DataInCentralDatabase.csv", header = None)
cf.fillna(value="N/A", inplace = True)

iterdate = iter(cf[9])
next(iterdate)
for i in iterdate:
    date = i
    date = datetime.striptime(date, '%Y%m%d').strftime('%d/%m%y')


cf[4].replace('Alexandria_stroe', 'Alexandria_store', inplace = True)
cf[11].replace('Alexandria_stroe', 'Alexandria_store', inplace = True)
trash = ['o?str 5538','eiter Weg 7765','ostenweg 2428','ostfach 99 92 92','rue de Linois','Mo str 5538',
'otth?user Weg 636','eiderplatz 662','8, avenue de l? Union Centrale','68, avenue de l?Europe','Ootth user Weg 636','unckerstr 22525']
cf[19].replace([trash], 'Unknown', inplace = True)
cf[25].replace(['9-Mar','9-May'], 'Unknown', inplace = True)

cf.to_csv("CleanedCD.csv", index = False, header = None)

