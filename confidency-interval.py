import numpy as np
import scipy.stats as st

# schema:Book nl
#data = [99,100,99,100,100,100,99,100,100,100]

# ore:Aggregation onb
data = [99,100,98,98,98,98,97,100,96,96]

# crear un intervalo de confianza del 95% 
print(st.t.interval(alpha = 0.95, df = len(data)-1, loc = np.mean(data), scale = st.sem(data)))


