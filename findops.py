import re

# Define a function to clean text by removing dates using regex
def clean_text(filename):
    with open(filename, 'r') as f:
        text = f.read()

    # regular expression to match dates in the format 'MMM DD, YYYY, H:MM AM/PM'
    regex = r'\b[A-Za-z]{3}\s\d{1,2},\s\d{4},\s\d{1,2}:\d{2}\s(?:AM|PM)\b'

    # remove all matches of the regular expression from the text
    return re.sub(regex, '', text)

# Clean the 'following.txt' file and write to 'followingoutput.txt'
following_cleaned = clean_text('following.txt')
with open('followingoutput.txt', 'w') as f:
    f.write(following_cleaned)

# Clean the 'followers.txt' file and write to 'followersoutput.txt'
followers_cleaned = clean_text('followers.txt')
with open('followersoutput.txt', 'w') as f:
    f.write(followers_cleaned)

# Read the cleaned files and convert to sets of usernames
with open('followingoutput.txt', 'r') as f1, open('followersoutput.txt', 'r') as f2:
    usernames1 = set(f1.read().split())
    usernames2 = set(f2.read().split())

# Find the symmetric difference of the sets to get the list of users that don't follow you back
unique_usernames = usernames1.symmetric_difference(usernames2)

# Sort usernames in alphabetical order
unique_usernames = sorted(list(unique_usernames), key=lambda x: (not x.isalnum(), x))

# Write the usernames to a text file called 'ops.txt'
if len(unique_usernames) == 0:
    print('There are no unique usernames.')
else:
    with open('ops.txt', 'w') as f:
        for username in unique_usernames:
            if username in usernames1:
                f.write(username + '\n')