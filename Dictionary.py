country_list = ['Malta',
 'Sudan',
 'Oman',
 'Jamaica',
 'Pakistan',
 'Netherlands',
 'Venezuela',
 'Tuvalu',
 'Kazakhstan',
 'Kazakhstan',
 'Congo {Democratic Rep}']

country_counts = {}
for country in country_list:
  if country in country_counts:
    country_counts[country] += 1
  else :
    country_counts[country] = 1
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
print (country_counts)
