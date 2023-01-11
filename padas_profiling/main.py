#pip install pandas
#pip install pandas-profiling
import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv("car_data.csv")
print(df)

#generate report
profile = ProfileReport(df)
profile.to_file(output_file="car.html")

###To get minimum info in the output
#profile = ProfileReport(df, minimal=True)
#profile.to_file(output_file="car.html")
