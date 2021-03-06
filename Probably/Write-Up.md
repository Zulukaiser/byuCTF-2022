# byuCTF 2022 Miscellaneous Probably

In this challenge we were provided with a netcat command and a python script. We can assume that the python script is running on the server that we can
listen to with the netcat command.
A quick look at the python script reveals, that we open a file called flagt.txt and randomize it in the function random_string()
the new randomized string gets build like this:
if a random number from 0 to 1 is less than 0.25 than the character of real character is appended to the new string. if the random number is greater or
equal to 0.25, a random letter number or an underscore is appended.
the new string gets returned and printed in ASCII-Art.
Unfortunately we can't decode the new string, so we have to do tedious work. The method i chose was simple:
- Get a moderate sized dataset
- compare characters
- choose most appearing characters.

So if we run the netcat command we get an output on our console like this:
cyu2td8ehoefsri_2hz_chp9cw6pynqua9cve

The flag most probably has th layout byuctf{SOME_THING}
so we can assume that the first characters are byuctf{?????????????????????????????}
and we know the length of the flags content which is 29 characters.
Now all we have to do is run the netcat command over and over, make a list out of the console output and search for the most common characters in each
column. Note that underscores can aslo be part of the flag. We can do this, because we have roughly a 1 in 4 chance, that the character thats printed
belongs to the flag. so 3 in 4 times the character doesn't belong to the flag. But if the character doesn't belong to the flag, it's a random character out
of 37 possibilities. But one of these 37 characters is coincidentally the right character. So the math behind this looks like this:
chance of right character: p = 1/4 + 3/4 * 1/37 = 10/37 =~ 27%
chance of individual wrong character: p = 3/4 * 1/36 =~ 2.1%

So in each column of the dataset the most common character should be the right character. If the dataset is too little, we can have false positives, so the
larger the dataset, the more chance we get the right character (rule of large numbers). Happy hunting!
