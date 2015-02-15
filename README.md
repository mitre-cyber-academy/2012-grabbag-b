 Title: Binary, binary everywhere and not a knot in site
Description: Time to start adding.

Challenge:
Give the students the file "findTheFlag.txt" and the Title & Description text above.

Note: One of the main files for this challenge is not located in this repository, it can be downloaded from here: [findTheFlag.txt](https://drive.google.com/file/d/0B48Lv30KB1seVDVHZ0ZNdkxERFk/view?usp=sharing).

Solution:

Team will probably start with something like following to add up the 1s

<count.py>
x = open("findTheFlag.txt", "r")
start = 0
    for y in x.readline():
    if y == str(1):        
start += int(y)
print start

Gives: 282349042

Should realize that needs to be massaged into another form.

Two potential paths from there

1) 
should use something like following script to find the hidden message:

x = open("findTheFlag.txt", "r")
for y in x.readline():    
if y != str(1):        
print y

Which produces:

s
u
m
i
n
h
e
x

With that, realize to convert to hex (could use the following website http://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html)
and get:

10D44DF2

Realize put MCA- in front, and done. (Flag MCA-10D44DF2)

2) Immediately try converting to hex and get to above.

Realize put MCA- in front, and done.
