# Python Programming Assignment #1
# Due: March 16th, at 11:59 pm
# Submission method -> Post to the cyberuniversity (see Lecture 2 for details).
# Fill in this blank with your student ID number: B073040022

# An anagram is created by rearranging the letters of a word or phrase to form
# a different word or phrase. Sometimes the anagram can seem related to the
# original phrase as: "Debit card" => "Bad credit", "Classroom" => "School
# master", or "Snooze alarms" => "Alas! No more Zs".

# In this homework we will create an anagram for "dormitory", by using the
# slicing, concatenation, and sorting operations and functions that we have
# covered in Lecture 2.

# You will create the anagram by filling in the blanks in the program below.
# Your solution must use exactly the set of letters that I've indicated, below.

# The code below uses the exec command. This command simply lets a string get
# executed as a command. For example: >>> s="print('Hi');print('Bye')"; exec(s)
# will print the same output as if you had typed: >>> print('Hi');print('Bye')

# The reason we use the exec command is so that your answer will be a string,
# named cmd. This lets us print the letters used with: print(sorted(set(cmd)))
# (Confused? See slide #115 of Lecture 2, where set('5.0') -> {'.', '0', '5'}).

# So with all of that out of the way, here is the program:
print()

s="dormitory"; t=" => "

cmd="p=sorted(s);print(s,t,p[:2]+p[-3:]+p[-4:1:-1])"
# In the above, you need to fill in the 2 blanks. Once that's done, execute it:

exec(cmd)
# Expected output of the previous line: dormitory  =>  ['d', 'i', 'r', 't', 'y', 'r', 'o', 'o', 'm']

# But what commands must you use to make to work? You'll only use commands that
# are covered in Lecture 2. It is helpful to see the letters in the solution:

print(sorted(set(cmd)))
# Expected output of the previous line: ['(', ')', '+', ',', '-', '1', '2', '3', '4', ':', ';', '=', '[', ']', 'd', 'e', 'i', 'n', 'o', 'p', 'r', 's', 't']
#     (If your output is different, then you'll need to try again. Now, what
#     commands will you use? Well, clearly you only use commands that can be
#     spelled with the letters d, e, i, n, o, p, r, s, and t. Moreover, we
#     already know that p, r, i, n, and t are used, since we see those letters
#     already, in the part of the cmd string that is already given to you.) 

print()

# In the second part, we'll do the reverse, creating an anagram for dirty room:
s="dirty room"
cmd="p=s[:1]+s[-2]+s[2]+s[9]+s[1]+s[1+2]+s[-2]+s[-2-2]+s[2+2];print(s,t,p)"
# In the above, you again fill in 2 blanks. Once that's done, you execute it:

exec(cmd)
# Expected output of the previous line: dirty room  =>  dormitory

print(sorted(set(cmd)))
# Expected output of the previous line: ['(', ')', '+', ',', '-', '1', '2', '9', ':', ';', '=', '[', ']', 'i', 'n', 'p', 'r', 's', 't']

print()
