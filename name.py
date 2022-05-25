from tracemalloc import Statistic
import plotly.figure_factory as ff 
import statistics
import random 
import pandas as pd
import csv
import plotly.graph_objects as go 

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
standard_deviation = statistics.stdev(data)
print("population mean:- ",population_mean)
print("standard deviation :-",standard_deviation)

#code to find mean and standard deviation of 100 data points 
def random_set_mean(counter):

    data_set = []
    for i in range(0,counter):
        ri = random.randint(0,len(data)-1)
        v = data[ri]
        data_set.append(v)
    mean = statistics.mean(data_set)
    std = statistics.stdev(data_set)    
    print("mean of sample : ",mean)
    print("standard deviation of sample :",std)
    return mean


#funcation to plot the mean on the graph 
def show_fig(mean_list):
    df = mean_list 
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y = [0,1],mode = "lines",name = "MEAN")) 
    fig.show()
    
def setup():
    mean_list = []
    for i in range(0,1000): 
        seto_of_means = random_set_mean(100)
        mean_list.append(seto_of_means)
    show_fig(mean_list)
setup()    