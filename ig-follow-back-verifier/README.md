# IG-Follow-Back-Verifier

IG-Follow-Back-Verifier is a Python program designed to help Instagram users identify which of their followers do not follow them back. This tool processes your Instagram followers and following lists, and provides a clear report of users who do not reciprocate your follow.

## Features

1. **Extracts Usernames:** Reads Instagram followers and following lists from text files.
2. **Compares Lists:** Identifies users who follow you but whom you do not follow back.
3. **Generates Report:** Outputs a list of non-reciprocal followers for easy review.

## How It Works

1. **Obtain Your Lists:**
   1. Go to the Instagram website on your desktop.
   2. Navigate to your profile.
   3. Access your followers and following lists.
   4. Copy the content of these lists into text files.

2. **Format the Lists:**
   1. Each line in your text files should include a username followed by 's profile picture.
   2. Example format: username's profile picture

3. **Prepare Your Files:**
   1. **Place the lists in the lists directory:**
      1. `followers_list.txt` for your followers.
      2. `following_list.txt` for the people you are following.
   2. **Check File Formatting:**
      1. Review the example files in the lists folder to understand the required format: `followers_list.txt` and `following_list.txt` demonstrate the correct format for your data.

## Usage

1. **Run the Program:** `python ig_follow_back_verifier.py`
2. **Check the Output:** The results will be saved in `lists/non_reciprocal_followers.txt`.

## Requirements

- Python 3.10

## Notes

- Ensure the `followers_list.txt` and `following_list.txt` files are correctly formatted for accurate results.
- This tool processes text files and does not interact with the Instagram API.
