# User profile 
def build_profile(first, last, **user_info):
    """ Build a dictionary containing everything we know about a user. """
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

# Call the function with different user information
user_profile1 = build_profile('albert', 'einstein', location='princeton', field='physics')
user_profile2 = build_profile('marie', 'curie', location='paris', field='chemistry', born=1867)
user_profile3 = build_profile('aleh', 'sitsko', location='grodno', field='unknown', born=1991, hobby='programming', profession='developer')
# Display the user profiles
print(user_profile1)
print(user_profile2)
print(user_profile3)