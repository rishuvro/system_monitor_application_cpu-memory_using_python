#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import psutil


# In[2]:


def monitor_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)  # Get CPU usage percentage
    cpu_label.config(text=f"CPU Usage: {cpu_percent}%")  # Update label text


# In[4]:


def monitor_memory():
    memory = psutil.virtual_memory()
    total_memory = memory.total // (1024 ** 2)  # Convert to MB
    used_memory = memory.used // (1024 ** 2)  # Convert to MB
    memory_percent = memory.percent

    memory_label.config(text=f"Memory Usage: {used_memory}MB / {total_memory}MB ({memory_percent}%)")


# In[5]:


root = tk.Tk()
root.title("System Monitoring App")


# In[6]:


cpu_label = tk.Label(root, text="CPU Usage: ")
cpu_label.pack()


# In[7]:


monitor_cpu_button = tk.Button(root, text="Monitor CPU", command=monitor_cpu)
monitor_cpu_button.pack()


# In[8]:


memory_label = tk.Label(root, text="Memory Usage: ")
memory_label.pack()


# In[9]:


monitor_memory_button = tk.Button(root, text="Monitor Memory", command=monitor_memory)
monitor_memory_button.pack()


# In[10]:


root.mainloop()


# In[ ]:




