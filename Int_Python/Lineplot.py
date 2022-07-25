import os

path = 'C:\\Users\\adasn\\Documents\\Datacamp\\DataCampWork\\Int_Python'
file_name = 'gapminder.csv'

complete_name = os.path.join(path, file_name)

print(complete_name)

# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap,life_exp)

# Display the plot
plt.show()