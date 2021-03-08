"""
You are given an integer  followed by  email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.


Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is 3.

⌨️ Input (n): ["3", "lara@hackerrank.com", "brian-23@hackerrank.com", "britts_54@hackerrank.com"]
🏆 Output: ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
🖥 https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter
"""

import re


regex = "^[0-9a-zA-Z-_]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]{1,3}$"


def validate_email(email):
    email = str(email)
    return re.match(regex, email)


def filter_mail(emails):
    return list(filter(validate_email, emails))


# input_emails = [3, "lara@hackerrank.com", "brian-23@hackerrank.com", "britts_54@hackerrank.com"]
# input_emails = ['regex_is_cool@python.org', 1]
input_emails = [2, "harsh@gmail", "iota_98@hackerrank.com"]

filtered_emails = sorted(filter_mail(input_emails))
print(filtered_emails)
