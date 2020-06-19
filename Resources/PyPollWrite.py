# Create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "W" mode we will write data to the file
Open(file_to_save, "W")