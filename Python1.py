#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Q1)x students & z subjects.
x,z=input("Enter number of students & number of subjects").split()
for i in range(int(x)):
    sum=0
    for j in range(int(z)):
        marks=int(input("Enter the marks"))
        sum=sum+marks
    print("Average marks for student",i+1,"=",sum/int(z))


# In[30]:


#Q2)
l1=[1,2,3,4,5]
s=int(input("Enter new element"))
k=int(input("Enter position"))
l1.insert(k-1,s)
print(l1)


# In[35]:


l1.remove(s)
print(l1)


# In[36]:


l1.append(s)
print(l1)


# In[37]:


l1.sort()
print(l1)


# In[38]:


l1.pop()
print(l1)


# In[43]:


l1.reverse()
print(l1)


# In[67]:


#Q3)
dict={"Pranay":[1,47,28,58],"Arjun":[8,29,37,6],"Yohan":[17,38,3,28]}
z=input("Enter student name")
for i in dict:
    if i==z:
        sum=0
        for j in dict[i]:
            sum=sum+j
        avg1=sum/len(dict[i])
        print(avg1)
        


#  """
# Keys in dictionary.
# dict={"Hi":[100,92,39]}
# for i in dict:
#     print(i)
# """

# In[11]:


#Q4)To check if email is in the correct format.
import re
def fun(s):
    if re.match(r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$",s)!=None:
        return(s)
    else:
        return("Pls check the format")
s=input("Enter an email")
fun(s)


# In[29]:


#Q5)
str=input("Enter a string")
z1=int(input("Enter index"))
z2=input("Enter an element")
str=str[:z]+z2+str[z+1:]
print(str)


# In[2]:


#Q6)
x = [10, 20, 30, 40, 10]
y = [75, 65, 35, 75, 30]
if x[0]==x[len(x)-1]:
  print("Elements are the same")
if y[0]==y[len(y)-1]:
  print("Elements are the same")


# In[12]:


#Q7)
for i in range(6):
  for j in range(i):
    print(i,end='')
  print('')  

