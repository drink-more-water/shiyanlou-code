#!/usr/bin/env python
# coding: utf-8

# In[11]:


y=int(input("Please enter an integer:"))
print(y)


def count(x):
    count=0
    num=0
    while x>1:
        if x%2==0:
            subcount=x/2
            x=x/2
        else:
            subcount=(x-1)/2
            x=(x-1)/2+1
        count=count+subcount
        num=num+1
        print("the {} round contains {} contests,and the total contests so far is {},remaining {} teams".format(num,subcount,count,x))
    return count

print(count(y))


# In[ ]:




