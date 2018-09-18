from __future__ import print_function

import pandas as pd
pd.__version__


cities = pd.Series(['san francisco', 'los angeles', 'sacramento'])
population = pd.Series([12314, 236234, 1451345])



dataframe = pd.DataFrame({"cities": cities, "population": population, "over 1 million": population.apply(lambda val: val > 1000000), "saint city": cities.apply(lambda name: name.startswith('san') )})







print(dataframe)