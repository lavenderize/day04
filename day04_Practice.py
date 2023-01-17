# 7.8
surprise = ["Groucho", "Chico", "Harpo"]

# 7.9
print(surprise[2].lower())
print(list(reversed(surprise)))
# print(surprise.capitalize())
surprise = [surprise.capitalize() for surprise in surprise]
print(surprise)
