import matplotlib.pyplot as plt

# Sample data
age_groups = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-99']
counts = [50, 120, 300, 450, 600, 550, 400, 200, 80, 20]

# Create bar chart
plt.bar(age_groups, counts, color='blue')
plt.xlabel('Age Groups')
plt.ylabel('Counts')
plt.title('Distribution of Ages in a Population')
plt.show()
