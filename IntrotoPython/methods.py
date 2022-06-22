# string to experiment with: place
place = "poolhouse"
str.upper(place)
place_up='POOLHOUSE'
# Use upper() on place: place_up
str.upper(place_up)

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count("o"))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
print(areas)
areas.append(15.45)
print(areas)


# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)