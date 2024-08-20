import re


def extract_usernames(file_path):
    """Extract names where each line ends with "'s profile picture"."""
    usernames = set()
    pattern = re.compile(r"^(.+?)'s profile picture$")

    with open(file_path, 'r') as file:
        for line in file:
            match = pattern.match(line.strip())
            if match:
                usernames.add(match.group(1))

    return usernames


def save_results(usernames, output_path):
    """Save the list of usernames to a file."""
    with open(output_path, 'w') as file:
        file.write('\n'.join(usernames))


def main():
    followers_file = 'lists/followers_list.txt'
    following_file = 'lists/following_list.txt'
    output_file = 'lists/non_reciprocal_followers.txt'

    # Extract usernames from files
    followers = extract_usernames(followers_file)
    following = extract_usernames(following_file)

    # Calculate non-reciprocal followers
    non_reciprocal_followers = following - followers

    # Print non-reciprocal followers
    print("Non-reciprocal followers:")
    for user in non_reciprocal_followers:
        print(user)

    # Save non-reciprocal followers to file
    save_results(non_reciprocal_followers, output_file)

    print(f"Non-reciprocal followers have been saved to {output_file}")


if __name__ == "__main__":
    main()
