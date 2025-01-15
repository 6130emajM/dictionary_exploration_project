# create_dictionary.py

# Step 1: Create a dictionary
favorite_movie = {
    "Title": "Inception",
    "Year of Release": 2010,
    "Genre": "Science Fiction",
    "Lead Actor/Actress": "Leonardo DiCaprio",
    "Rating": 9
}

# Step 2: Access and print values for "Title" and "Rating"
print("Movie Title:", favorite_movie["Title"])
print("Movie Rating:", favorite_movie["Rating"])

# Step 3: Update the "Rating" to a new value
favorite_movie["Rating"] = 9.5
print("Updated Dictionary:", favorite_movie)

# Step 4: Add a new key-value pair for "Director"
favorite_movie["Director"] = "Christopher Nolan"
print("Dictionary after adding 'Director':", favorite_movie)

# Step 5: Remove the "Genre" key
del favorite_movie["Genre"]
print("Dictionary after removing 'Genre':", favorite_movie)