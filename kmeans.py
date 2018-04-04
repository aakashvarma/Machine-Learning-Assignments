def from_str(dataset, attrs):

    if type(attrs) == list:
        for attr_name in attrs:
            dataset[attr_name] = dataset[attr_name].astype(float)

    else:
        data[attrs] = data[attrs].astype(float)
    
return dataset

