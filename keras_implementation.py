from keras.models import Sequentialfrom keras.layers import Densefrom keras.wrappers.scikit_learn import KerasClassifierfrom keras.utils import to_categoricalfrom sklearn.model_selection import StratifiedKFoldfrom sklearn.model_selection import cross_val_scorefrom sklearn.preprocessing import LabelEncoderfrom sklearn.pipeline import Pipelineimport numpy as npimport pandas as pddef create_model():	model = Sequential()	model.add(Dense(12, input_dim=8, activation='relu'))	model.add(Dense(8, activation='relu'))	model.add(Dense(1, activation='sigmoid'))	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])	return modeldef separateFeaturesTarget(df):     features=df[['Countries','Number of speakers','Latitude','Longitude']].iloc[0:].values    target=df[['Degree of endangerment']].iloc[0:].values.ravel()    return features, targetdef cleanCountries(arr):    row=0    countriesDict={}    languageCountries=[]    count=0    for x in arr:         countryList=[0]*85        x=str(x)        row=row+1        country=''        for y in range(0,len(x)):            if x[y]==',' or y==len(x):                country=country.strip()                if country not in countriesDict:                    countriesDict[country]=count                    count=count+1                countryList[count-1]=1                country=''            else:                 country+=x[y]        languageCountries.append(countryList)    return languageCountries                    def cleanNumerics(arr):    arr[np.isnan(arr)] = np.median(arr[~np.isnan(arr)])    for x in range(0,len(arr)):        arr[x]=float(arr[x])    return arrdef cleanTarget(arr):    for x in range (0,len(arr)):         if arr[x]=='Vulnerable':            arr[x]=0        elif arr[x]=='Severely Endangered':            arr[x]=1        elif arr[x]=='Definitely Endangered':            arr[x]=2        elif arr[x]=='Severely Endangered':            arr[x]=3        elif arr[x]=='Extinct':            arr[x]=4    return arr            def readData():     extinctLanguages=pd.read_csv("extinctLanguages.csv")    extinctLanguages.fillna(0)    extinctLanguages['Degree of endangerment']=cleanTarget(extinctLanguages['Degree of endangerment'])    extinctLanguages['Countries']=cleanCountries(extinctLanguages['Countries'])    extinctLanguages['Number of speakers']=cleanNumerics(extinctLanguages['Number of speakers'])    extinctLanguages['Latitude']=cleanNumerics(extinctLanguages['Latitude'])    extinctLanguages['Longitude']=cleanNumerics(extinctLanguages['Longitude'])    extinctLanguageFeatures, extinctLanguageTarget=separateFeaturesTarget(extinctLanguages)        readData()    