#!/usr/bin/env python
# coding: utf-8

# In[1]:


import googletrans
from googletrans import Translator
from gtts import gTTS


# In[2]:


lang_list=(dict(googletrans.LANGUAGES))


# In[3]:


lang_list


# In[4]:


text1 ="hello how are you"
text2 ="ಅವನು ಹುಡುಗ"


# In[5]:


translator=Translator() 


# In[6]:


print(translator.detect(text2))


# In[7]:


res1= translator.translate(text1, src='en',dest='kn')
print(res1)


# In[8]:


res2= translator.translate(text2, src='kn',dest='hi')
print(res2)


# In[9]:


print(res2.text)


# In[10]:


print(res2.pronunciation)


# In[11]:


print(res2.extra_data)


# In[12]:


print(res2.extra_data['origin_pronunciation'])


# In[13]:


lang_list['kn']


# In[19]:


audio_res= gTTS(text= res2.text, lang='hi')


# In[20]:


audio_res.save("audio.mp3")


# In[ ]:





# In[ ]:





# In[ ]:




