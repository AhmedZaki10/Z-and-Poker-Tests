#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Poker Test
import scipy.stats as stats
import pandas as pd

# Given probabilities
probabilities = {
    'five_different_digits': 0.3024,
    'pair': 0.504,
    'two_pairs': 0.108,
    'three_of_a_kind': 0.072,
    'full_house': 0.009,
    'four_of_a_kind': 0.0045,
    'five_of_a_kind': 0.0001  # Corrected to 0.0001 to sum up to 1
}

# Observed frequencies
observed_frequencies = {
    'five_different_digits': 3075,
    'pair': 4935,
    'two_pairs': 1135,
    'three_of_a_kind': 695,
    'full_house': 105,
    'four_of_a_kind': 54,
    'five_of_a_kind': 1
}

# Total number of observations
total_observations = sum(observed_frequencies.values())

# Calculate expected frequencies
expected_frequencies = {category: total_observations * probability for category, probability in probabilities.items()}

# Perform chi-square test
chi_square_statistic, p_value = stats.chisquare(list(observed_frequencies.values()), list(expected_frequencies.values()))

# Determine critical value at alpha = 0.01
alpha = 0.01
degrees_of_freedom = len(observed_frequencies) - 1
critical_value = stats.chi2.ppf(1 - alpha, degrees_of_freedom)

# Print results
print("Chi-square Test Statistic:", chi_square_statistic)
print("Critical Value:", critical_value)
print("P-value:", p_value)

# Make decision
if chi_square_statistic > critical_value:
    print("Reject the null hypothesis. The numbers are not independent.")
else:
    print("Fail to reject the null hypothesis. The numbers are independent.")

# Observed and expected frequencies
data = {
    'Category': ['Five different digits', 'Pair', 'Two pairs', 'Three of a kind', 'Full house', 'Four of a kind', 'Five of a kind'],
    'Observed Frequency': [3075, 4935, 1135, 695, 105, 54, 1],
    'Expected Frequency': [expected_frequencies[category] for category in probabilities.keys()]
}

# Create DataFrame
df = pd.DataFrame(data)

df['Chi-square Value'] = ((df['Observed Frequency'] - df['Expected Frequency']) ** 2) / df['Expected Frequency']

styled_df = df.style.set_properties(**{'text-align': 'center'}) 
styled_df


# In[2]:


# Z method.

import numpy as np

def z_autocorrelation(numbers):
    n = len(numbers)
    mean = np.mean(numbers)
    std_dev = np.std(numbers)
    
    # Calculate autocorrelation using Z method
    z = [(numbers[i] - mean) / std_dev for i in range(n - 1)]
    autocorrelation = np.mean([z[i] * z[i - 1] for i in range(1, n - 1)])
    
    return autocorrelation

# Given numbers
numbers = [0.37, 0.55, 0.71, 0.97, 0.65, 0.29, 0.81, 0.78, 0.23]

# Calculate autocorrelation using Z method
autocorrelation = z_autocorrelation(numbers)

print("Autocorrelation using Z method:", autocorrelation)

# Threshold for rejection
threshold = 0.1

# Determine if the test is rejected or not
if abs(autocorrelation) > threshold:
    print("Reject the null hypothesis. Autocorrelation is significant.")
else:
    print("Fail to reject the null hypothesis. Autocorrelation is not significant.")

