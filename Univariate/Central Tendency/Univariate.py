class univariate():
    def quanqual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            if dataset[columnName].dtype=='str':
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual


    def freqTable(columnName,dataset):
        freqTable=pd.DataFrame(columns=['Unique_values','frequency','relative_frequency','cumulative_freqency'])
        freqTable['Unique_values']=dataset[columnName].value_counts().index
        freqTable['frequency']=dataset[columnName].value_counts().values
        freqTable['relative_frequency']=freqTable['frequency']/103
        freqTable['cumulative_freqency']=freqTable['relative_frequency'].cumsum()
        return freqTable

    def univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR",'Lesser','Greater','Min','Max'],columns=quan)
        for columnName in quan:
            descriptive.loc["Mean",columnName]=dataset[columnName].mean()
            descriptive.loc["Median",columnName]=dataset[columnName].median()
            descriptive.loc["Mode",columnName]=dataset[columnName].mode()[0]
            descriptive.loc["Q1:25%",columnName]=dataset.describe().loc["25%",columnName]
            descriptive.loc["Q2:50%",columnName]=dataset.describe().loc["50%",columnName]
            descriptive.loc["Q3:75%",columnName]=dataset.describe().loc["75%",columnName]
            descriptive.loc["99%",columnName]=np.percentile(dataset[columnName],99)
        
            descriptive.loc["Q4:100%",columnName]=dataset.describe().loc["max",columnName]
            descriptive.loc["IQR",columnName]=descriptive.loc["Q3:75%",columnName]-descriptive.loc["Q1:25%",columnName]
            descriptive.loc["Lesser",columnName]=descriptive.loc["Q1:25%",columnName]-(1.5)*descriptive.loc["IQR",columnName]
            descriptive.loc["Greater",columnName]=descriptive.loc["Q3:75%",columnName]+(1.5)*descriptive.loc["IQR",columnName]
            descriptive.loc["Min",columnName]=dataset[columnName].min()
            descriptive.loc["Max",columnName]=dataset[columnName].max()
        return descriptive


    def outlierDetection(quan, descriptive):
        lesser_outlier = []
        greater_outlier = []
    
        for columnName in quan:
            if descriptive.loc['Min', columnName] < descriptive.loc['Lesser', columnName]:
                lesser_outlier.append(columnName)
    
            if descriptive.loc['Max', columnName] > descriptive.loc['Greater', columnName]:
                greater_outlier.append(columnName)
    
        print("Lesser Outliers:", lesser_outlier)
        print("Greater Outliers:", greater_outlier)
    
        return lesser_outlier, greater_outlier

    def replaceOutlier(lesser_outlier, greater_outlier, descriptive, dataset):
        for columnName in lesser_outlier:
            lower = descriptive.loc['Lesser', columnName]
    
            dataset.loc[dataset[columnName] < lower, columnName] = lower
    
        print("Lower outliers replaced successfully")
    
        for columnName in greater_outlier:
            higher = descriptive.loc['Greater', columnName]
    
            dataset.loc[dataset[columnName] > higher, columnName] = higher
    
        print("Higher outliers replaced successfully")
    
        return dataset