#Calculate Value of PI using the Neelkantha method to nth digit using upto 50 trailing digits
import numpy as np
kaggle = input('Enter value of n upto which you want to display the value of PI:')
a = '%.'+kaggle+'f'
print (a%(np.e))