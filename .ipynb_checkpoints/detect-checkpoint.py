import admin_functions as adfn

#==============================================    
def sz_thresh(mean, scalar, percentile):
#==============================================    
    """
    This calculates a baseline and applies sliding window along brain sum time series to find any points above threshold from baseline as seizure events. 
    
    Inputs:
        mean (np array): 1d vector timeseries
        scalar (int): threshold for seizure
        percentile (int): nth percentile to calculate baseline
    
    Returns:
        sz_index (list): time indices of seizure events
    
    """
    import numpy as np
    
    window = adfn.window(50, mean.shape[0])[0]

    #Calculate baseline
    baseline = np.zeros(mean.shape[0])
    for i in range(mean.shape[0]):
        baseline[i] = (np.mean(mean[np.where(mean < np.quantile(mean, percentile, axis=0))]))
        
    meanbase = np.mean(baseline)
    sz_index = []
    
    #Apply sliding window over mean trace - any values above scalar * mean baseline are seizures
    #sz index as any values above baseline 
    for e in range(mean.shape[0]):
        if np.mean(mean[e:e+window]) > scalar*meanbase:
            sz_index = np.append(sz_index, e)
            
    return(sz_index)