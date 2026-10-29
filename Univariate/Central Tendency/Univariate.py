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