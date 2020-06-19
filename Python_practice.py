counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{"county":"Arapahoe", "registered_voters":422829},{"county":"Denver","registered_voters":463353}]
for county, voters in counties_dict.items():
    print(f"{county} has {voters} registered voters")






