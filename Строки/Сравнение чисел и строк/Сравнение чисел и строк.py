master_age = 13
user_age = 8

print(user_age > master_age)

master_age = "13"
user_age = "8"

print(user_age > master_age)

master_age = "ac"
user_age = "h"

print(user_age > master_age)  # h > a

master_age = "ac"
user_age = "ah"

print(user_age > master_age)  # a = a,  c < h

master_age = "13"
user_age = "18"
master_age = int(master_age)
user_age = int(user_age)

print(user_age > master_age)
