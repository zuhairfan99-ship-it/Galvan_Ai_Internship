# video 3
# Print Welcome Message
message = "Hello World"
print(message)
print("Hello Zuha")

txt = "Bobby's World"  # or 'Bobby\'s World'
print(len(txt))

# silicing
print(txt[0])
print(txt[0:5])
print(txt[6:7])
print(txt.lower())
print(txt.upper())
print(txt.count('b'))
print(txt.find('World'))

n = txt.replace('World', 'Universe')
print(n)

# Concatenation
g = 'Hello'
name = 'Zoya'

c = g + ',' + name + ',' + 'Welcome'
print(c)

c = '{}, {}, Welcome!'.format(g, name)
print(c)

c = f'{g}, {name}, Welcome!'  # f-string
print(c)

print(dir(name))
# print(help(str))
# print(help(str.lower()))

# video 5
# Comparison Operation
language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

# and,or,not
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

#
user = 'Admin'
logged_in = False

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

#
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
print(id(a) == id(b))

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#
nums = [1, 2, 3, 4, 5]

for i in nums:
    if i == 3:
        print('Found!')
        continue
    print(i)

# video 6
nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter)

#
for i in range(1, 11):
    print(i)

#
x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1

# video 7
person = {'name': 'Jenn', 'age': 23}

tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

sentence = "My name is {0[name]} and I am {0[age]} years old.".format(person)
print(sentence)

l = ['Jenn', 23]

sentence = "My name is {0[0]} and I am {0[1]} years old.".format(l)
print(sentence)

#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

#
sentence = 'My name is {name} and I am {age} years old.'.format(
    name='Jenn', age='30'
)
print(sentence)

#
person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)

#
for i in range(1, 11):
    sentence = 'The value is {}'.format(i)
    print(sentence)

#
pi = 3.14159265

sentence = 'Pi is equal to {:.3f}'.format(pi)
print(sentence)

#
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000 ** 2)
print(sentence)

#
import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

###
# March 01, 2016
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# March 81, 2016 fell on a Tuesday and was the 861 day of the year.
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)

# video 8
##
import datetime
import pytz

d = datetime.date(2016, 7, 24)
print("Specific Date:", d)

tday = datetime.date.today()
print("Today's Date:", tday)

print("Year:", tday.year)
print("Month:", tday.month)
print("Day:", tday.day)

print("Weekday (Monday=0, Sunday=6):", tday.weekday())
print("ISO Weekday (Monday=1, Sunday=7):", tday.isoweekday())

####
tdelta = datetime.timedelta(days=7)

print("Date 7 days from now:", tday + tdelta)
print("Date 7 days ago:", tday - tdelta)

bday = datetime.date(2016, 9, 24)
till_bday = bday - tday

print("Time until birthday:", till_bday)
print("Days until birthday:", till_bday.days)
print("Seconds until birthday:", till_bday.total_seconds())

####
t = datetime.time(9, 30, 45, 100000)
print("Time Object:", t)
print("Hour:", t.hour)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print("Datetime Object:", dt)

print("Date part:", dt.date())
print("Time part:", dt.time())

dt_delta = datetime.timedelta(hours=12)
print("12 hours later:", dt + dt_delta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print("dt.today():", dt_today)
print("dt.now():", dt_now)
print("dt.utcnow():", dt_utcnow)

dt_aware = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
print("Aware UTC Datetime:", dt_aware)

dt_now_utc = datetime.datetime.now(tz=pytz.UTC)
print("Current Aware UTC Time:", dt_now_utc)

dt_mountain = dt_now_utc.astimezone(pytz.timezone('US/Mountain'))
print("Mountain Time:", dt_mountain)

dt_naive = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')

dt_mountain_aware = mtn_tz.localize(dt_naive)
print("Localized Mountain Time:", dt_mountain_aware)

dt_eastern = dt_mountain_aware.astimezone(pytz.timezone('US/Eastern'))
print("Eastern Time:", dt_eastern)

####
print("ISO Format:", dt_mountain_aware.isoformat())

dt_str = dt_mountain_aware.strftime('%B %d, %Y')
print("Formatted String (strftime):", dt_str)

str_to_dt = datetime.datetime.strptime('July 26, 2016', '%B %d, %Y')
print("Parsed Datetime (strptime):", str_to_dt)

# video 9
f = open('test.txt', 'r')

print("File name:", f.name)
print("File mode:", f.mode)

f.close()

####
with open('test.txt', 'r') as f:
    pass

print("Is file closed?:", f.closed)

##
# Option A: Read entire contents at once
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

# Option B: Read all lines into a list
with open('test.txt', 'r') as f:
    f_lines = f.readlines()

# Option C: Read line by line manually
with open('test.txt', 'r') as f:
    f_line = f.readline()
    print(f_line, end='')

    f_line = f.readline()
    print(f_line, end='')

# Option D: Iterate line by line
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

# Option E: Read in fixed chunk sizes using a loop
with open('test.txt', 'r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:  # [00:11:00]
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)

####
with open('test.txt', 'r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print("\nCurrent pointer position:", f.tell())

    f.seek(0)

    f_contents = f.read(size_to_read)

####
with open('test2.txt', 'w') as f:
    f.write('Test')
    f.write('Test')

    f.seek(0)
    f.write('R')

####
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

####
with open('bronx.jpeg', 'rb') as rf:
    with open('bronx_copy.jpeg', 'wb') as wf:
        chunk_size = 4096

        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)