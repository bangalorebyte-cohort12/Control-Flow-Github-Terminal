

# Control flow via indentation




if 2**2 == 4:
    print('Obvious!')

# luckily ipython does the indentation whenever we move to a new line
# but if we did the following

if 2**2 ==4:
print('Obviously Not!')

#the interpreter tells us in this case where and how we went wrong


# Iteration

counter = 1
while counter <= 5:
    print("Hello, world")

# compound condition


done = True
while counter <= 10 and not done:
    print("hello")
    
# the value of the variable counter would need to be less than or
# equal to 10 and the value of the variable done would need to be False 
# (not False is True) so that True and True results in True.


# In[14]:


z = 1 + 1j
while abs(z) < 100:
    if z.imag == 0:
        break
    z = z**2 + 1



# THE FOR LOOP

for item in [1,3,6,2,5]:
    print(item)

# This works for any sequence (lists, tuples, and strings).

for item in range(5):
    print(item**2)



# nested for loops
wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)

# Example of Nested For Loop: Grading

score = 65
if score >= 90:
   print('A')
else:
   if score >=80:
      print('B')
   else:
      if score >= 70:
         print('C')
      else:
         if score >= 60:
            print('D')
         else:
            print('F')


# Avoiding For Loops using elif. Elif is like the "or" statment

if score >= 90:
   print('A')
elif score >=80:
   print('B')
elif score >= 70:
   print('C')
elif score >= 60:
   print('D')
else:
   print('F')


# List Comprehension: Syntactic Sugar
# Avoids looking up append attribute of the list, loaded and called as
# a function, which takes time and that adds up over iterations.

sqlist=[]
for x in range(1,11):
    sqlist.append(x*x)


sqlist=[x*x for x in range(1,11)]






