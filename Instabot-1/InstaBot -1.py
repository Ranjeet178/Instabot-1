#!/usr/bin/env python
# coding: utf-8

# 1. Login to your Instagram Handle
# 
#      1.Submit with sample username and password

# In[2]:


from selenium import webdriver                                    #importing webdriver
from selenium.webdriver.support.ui import WebDriverWait           #To use implcit and explicit wait
from selenium.webdriver.support import expected_conditions as EC  #use in explicitly wait
from selenium.webdriver.common.by import By                       #to select the attribute by Class,link_text
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup                                              #work with attribute 
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException  #to handle StaleElementReferenceException
from selenium.webdriver.common.keys import Keys #For navigating the pop up window
from selenium.common.exceptions import NoSuchElementException #to handle NoSuchElementException


# In[3]:


driver=webdriver.Chrome(executable_path='C:/Users/singh/chromedriver') #path of 
driver.get('https://www.instagram.com/') #navigating to the instagram log in page
wait = WebDriverWait(driver, 10)
name= wait.until(EC.presence_of_element_located((By.NAME,'username'))) #locating the box to insert name of the user
name.send_keys('sample_username') # passing username
pas=driver.find_element_by_name('password') # locating the box to insert the password of the user
pas.send_keys('sample_password') #passinf password
login=driver.find_element_by_class_name('L3NKy') #serch for login button
login.click() #clicking on the login button


# 2. Type for “food” in search bar and print all the names of the Instagram Handles that are displayed in list after typing “food”
#    1. Note : Make sure to avoid printing hashtags

# In[4]:


search=driver.find_element_by_xpath('//input[contains(@class,"XTCLo")]') #loacting the search box
search.send_keys("food")                                                #sending values for searching
time.sleep(3)
val=driver.find_elements_by_xpath('//div[@class = "fuqBx"]/a["href"]')  #fetching food list Handles 
food=[] #creating an empty list for appending the list of food handlers
for i in val:
    if 'explore' in i.get_attribute('href'):        #if explore present in link then it is hastags
        continue
    else:
        s = i.get_attribute('href').split('/')      #https://www.instagram.com/foodtalkindia
        print(s[3])                                     # after split s= ['https:','','www.instagram.com','stockholmfood']
        food.append(s[3])                          #appending s[3] in food_list       
a=driver.find_element_by_xpath('//input[contains(@class,"XTCLo")]')  #seaeching  input box 
a.clear() #clearing the input  box
b=driver.find_element_by_class_name('coreSpriteSearchClear').click() #selecting clear box by class name and clicking it


# 3. Searching and Opening a profile using 
#   
#   A. Open profile of “So Delhi” 

# In[5]:


search=driver.find_element_by_xpath('//input[contains(@class,"XTCLo")]') #loacting the search box
search.send_keys("So Delhi")                                              #sending values for searching
b = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'yCE8d')))     #selecting so delhi
b.click() #clicking it to move to the profile of so delhi
a=driver.find_element_by_class_name('coreSpriteSearchClear') #selecting clear box by class name
a.click()


# In[6]:


driver.back()


# 4. Follow/Unfollow given handle - 
#    
#    A. Open the Instagram Handle of “So Delhi”

# In[7]:


search=driver.find_element_by_xpath('//input[contains(@class,"XTCLo")]') #loacting the search box
search.send_keys("So Delhi")                                              #sending values for searching
b = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'yCE8d')))     #selecting so delhi
b.click() #clicking it to open  the profile of "so delhi"


# B.Start following it. Print a message if you are already following

# In[12]:


follow= wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(@class,"vBF20")]/button')))  #locating the follow button
if follow.text.strip() == 'Follow':      #checking if the status is following or not
    follow.click() #if not following clicking on the follow button
else:
   print("you are already a follower of this account")    #printing you are not a follower                       


# C. After following, unfollow the instagram handle. Print a message if you have already unfollowed.                                                                  

# In[13]:


if follow.text.strip()!='Follow': #checking if the status is following or not
    unfollow=wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(@class,"vBF20")]/button')))  #locating and clicking following button
    unfollow.click()
    unfollow=wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"mt3GC")]/button'))) #locating the unfollow button
    unfollow.click() #clicking the unfollow button
else:
    print("you are already not a follower of this account") #printing if you are not following this account.


# In[ ]:


z556c


# 5. Like/Unlike posts
#   
#     A. Liking the top 30 posts of the ‘dilsefoodie'. Print message if you have

# In[14]:


driver.back() #navigating back to the home page


# In[15]:


search=driver.find_element_by_xpath('//input[contains(@class,"XTCLo")]') #loacting the search box
search.send_keys("dilsefoodie")                                              #sending values for searching
d=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'z556c')))            #searching dilsefoodie profile  
d.click()                                                                     #clicking on profile
for i in range(3):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')        #infirst scroll we get 12 post so we making 3
    time.sleep(2)                                     
post = driver.find_elements_by_xpath('//div[contains(@class,"v1Nh3")]')            #finding post 
count = 1
for i in post:
    if count >30: 
         break
    i.click()  #clicking the post
    like_btn = wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(@class,"fr66n")]/button'))) #locating like button
    data=BeautifulSoup(driver.page_source,'lxml') #reading and parsing data using beautifulsoap
    chk_like=data.find(class_='fr66n') #locating the class for checking whether it is like or not
    if chk_like.button.svg['aria-label']=='Unlike': #if it is "unlike" then you already liked the post
        print("you already liked the post no.",count,"Post")#for like button
    else:
        like_btn.click() 
    close_btn = wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"BI4qX")]/button'))) # post close button
    close_btn.click()                                                              #click on close utton
    time.sleep(1)
    count += 1


# B. Unliking the top 30 posts of the ‘dilsefoodie’. Print message if you have already unliked it.

# In[16]:


count = 1
for i in post:
    if count >30: 
         break
    i.click() 
    like_btn = wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(@class,"fr66n")]/button')))
    data=BeautifulSoup(driver.page_source,'lxml') #reading and parsing data using beautifulsoap
    chk_like=data.find(class_='fr66n') #locating the class for checking whether it is like or not
    if chk_like.button.svg['aria-label']=='Unlike': #if it is "unlike" then you already liked the post
        like_btn.click()
       
    else:
        print("you already unliked the post no.",count,"Post")#for like button    
    close_btn = wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"BI4qX")]/button'))) # locating post close button
    close_btn.click()         #clicking on close utton
    time.sleep(1)
    count += 1   #counting number of post


# 6. Extract list of followers
# 
# A. Extract the usernames of the first 500 followers of ‘foodtalkindia’ and ‘sodelhi’.                                            

# In[18]:





# In[19]:


search=driver.find_element_by_xpath('//input[contains(@class,"XTCLo")]') #loacting the search box
search.send_keys("foodtalkindia")                                              #sending values for searching
b = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'yCE8d')))     #selecting foodtalkindia
b.click() #clicking it to open  the profile of "foodtalkindia"

followers_button = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(@class,"-nal3")]'))) #follower button search
followers_button.click()   #click on followers button
time.sleep(3)
while True:
    f= driver.find_element_by_class_name('isgrP') #locating the #follower page
    f.click()
    driver.find_element_by_tag_name('body').send_keys(Keys.END) #moving end of document 
    follower= driver.find_elements_by_xpath('//div[@class = "isgrP"]/ul/div/li') #follower list
    if len(follower)>=500: #checking whether the count is greated then 500 or not
        break

li = []
j=0
foodtalkindia= [] #empty list to store the user names
for i in follower:                                                                  
    data = BeautifulSoup(i.get_attribute('innerHTML'),'html')                         #to get the name of follower             
    li.append(data.a['href'].split('/')[1])                                           #adding name in list
    foodtalkindia.append(data.a['href'].split('/')[1])
    j+=1
    if j==500:                                                                        #only top 500 follower
        break
for i in foodtalkindia:
    print(i) #printing all the names


# In[20]:


driver.back()
driver.back()


# soDELhi

# In[21]:


search=driver.find_element_by_xpath('//input[contains(@class,"XTCLo")]') #loacting the search box
search.send_keys("sodelhi")                                              #sending values for searching
b = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'yCE8d')))     #selecting sodelhi
b.click() #clicking it to open  the profile of "sodelhi"

followers_button = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(@class,"-nal3")]'))) #follower button search
followers_button.click()   #click on followers button
time.sleep(2)
while True:
    f= driver.find_element_by_class_name('isgrP') #locating the #follower page
    f.click()
    driver.find_element_by_tag_name('body').send_keys(Keys.END)  #moving end of document 
    follower= driver.find_elements_by_xpath('//div[@class = "isgrP"]/ul/div/li') #follower list
    if len(follower)>=500: #checking whether the count is greated then 500 or not
        break

li = []
j=0
sodelhi= []
for i in follower:                                                                  
    data = BeautifulSoup(i.get_attribute('innerHTML'),'html')                         #to get the name of follower             
    li.append(data.a['href'].split('/')[1])                                           #adding name in list
    sodelhi.append(data.a['href'].split('/')[1])
    j+=1
    if j==500:                                                                        #only top 500 follower
        break
for i in sodelhi:#running a loop to display all the to 500 followers
    print(i)


# In[22]:


driver.back()
driver.back()


# B. Now print all the followers of “foodtalkindia” that you are following but those who don’t follow you.

# In[23]:


search=driver.find_element_by_xpath('//input[contains(@class,"XTCLo")]') #loacting the search box
search.send_keys("foodtalkindia")                                             #sending values for searching
b = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'yCE8d')))     #selecting foodtalkindia
b.click() #clicking it to open  the profile of "foodtalkindia"
followers_button = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(@class,"-nal3")]'))) #follower button search
        #da=BeautifulSoup(driver.page_source,'lxml')
        #allfoll=int(da.find_all(class_='g47SY')[1]['title'].replace(',',''))
followers_button.click()   #click on followers button
time.sleep(2)
while True:
    f= driver.find_element_by_class_name('isgrP') #locating the #follower page
    f.click()
    driver.find_element_by_tag_name('body').send_keys(Keys.END)  #moving end of document
    follower= driver.find_elements_by_xpath('//div[@class = "isgrP"]/ul/div/li') #follower list
    if len(follower) >= 500:
        break  #checking whether the count is greated then 500 or not
    

li = [] #creating an empty list
j=0 #creating this variable to keep track of the count
names = [] #emptylist for storing the name of the user
for i in follower:
    data = BeautifulSoup(i.get_attribute('innerHTML'),'html')
    li.append(data.a['href'].split('/')[1])
    names.append(data.a['href'].split('/')[1])
    j+=1
    if j==500:
        break


i=0 #this variable I have created to have the index value throungh which we can determine the name of the user
for p in follower:
    try:
        data = BeautifulSoup(p.get_attribute('innerHTML'),'html')
        if data.button.text=="Following":   #only printing that follwoing but don't follow u back 
            print(names[i])
        
        i=i+1

    except StaleElementReferenceException:
        continue
       


# 7. Check the story of ‘coding.ninjas’. Consider the following Scenarios and print error messages accordingly -

# A. If You have already seen the story.
# 
# B. Or The user has no story.
# 
# c. Or View the story if not yet seen.

# In[24]:


driver.back()
driver.back()


# In[28]:


search=driver.find_element_by_xpath('//input[contains(@class,"XTCLo")]') #loacting the search box
search.send_keys("coding.ninjas")                                             #sending values for searching
b = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'yCE8d')))     #selecting coding.ninjas
b.click() #clicking it to open  the profile of "coding.ninjas"
time.sleep(2)
try:
    #i have compared the width of the canvas class when it is seen its value is 208 and have different value when its is not seen
    if int(driver.find_element_by_xpath('//div[contains(@class, "h5uC0")]/canvas').get_attribute('height'))==208:
        print('You have already seen the story!')#printing the status
    elif int(driver.find_element_by_xpath('//div[contains(@class, "h5uC0")]/canvas').get_attribute('height'))!=208:
        print("You have not seen the story and you will be redirected to the status page")#printing the status
        driver.find_element_by_xpath('//div[contains(@class, "h5uC0")]').click()#redirecting to the status page to view the status
except NoSuchElementException:
    print('The user has no story!')


# In[ ]:





# In[ ]:




