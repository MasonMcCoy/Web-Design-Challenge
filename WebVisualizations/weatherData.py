import pandas

data = pandas.read_csv(".\Resources\cities.csv")
weatherDF = pandas.DataFrame(data)
pandas.DataFrame.to_html(weatherDF)