import random
import pandas as pd
import category_encoders as ce
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
#data.head() 

df = ce.OneHotEncoder(cols = "whoAmI")
data = df.fit_transform(data)
data.head()



#data = pd.get_dummies(data['whoAmI'])
#data.head()