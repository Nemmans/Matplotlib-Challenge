#!/usr/bin/env python
# coding: utf-8

# ## Observations and Insights 

# 

# In[4]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st

# Study data files
mouse_metadata_path = "data/Mouse_metadata.csv"
study_results_path = "data/Study_results.csv"

# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

# Combine the data into a single dataset
combined_df = pd.merge(mouse_metadata, study_results, how = "inner", on = "Mouse ID")

# Display the data table for preview
combined_df


# In[5]:


# Checking the number of mice.
mouse_count = combined_df["Mouse ID"].count()
mouse_count


# In[8]:


# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint. 
# Stack Overflow for Syntax
duplicate_mice = combined_df[combined_df.duplicated(["Mouse ID", "Timepoint"])]
duplicate_mice


# In[9]:


# Optional: Get all the data for the duplicate mouse ID. 
#Review


# In[11]:


# Create a clean DataFrame by dropping the duplicate mouse by its ID.
clean_df = combined_df.drop_duplicates("Mouse ID")
clean_df


# In[13]:


# Checking the number of mice in the clean DataFrame.
mouse_count_clean = clean_df

#249 rows in clean df--> 249 mice


# ## Summary Statistics

# In[15]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: 
# mean, median, variance, standard deviation, and SEM of the tumor volume. 
# Assemble the resulting series into a single summary dataframe.

mean = combined_df.groupby('Drug Regimen')['Tumor Volume (mm3)'].mean()
median = combined_df.groupby('Drug Regimen')['Tumor Volume (mm3)'].median()
variance = combined_df.groupby('Drug Regimen')['Tumor Volume (mm3)'].var()
standard_dv = combined_df.groupby('Drug Regimen')['Tumor Volume (mm3)'].std()
sem = combined_df.groupby('Drug Regimen')['Tumor Volume (mm3)'].sem()

summary_df = pd.DataFrame({"Mean": mean, "Median": median, "Variance": variance, "Standard Deviation": standard_dv, "SEM": sem})
summary_df

# Thank you Sharon for the assist with mm3 syntax


# In[17]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen
# See above?
# Using the aggregation method, produce the same summary statistics in a single line
# See above?


# ## Bar and Pie Charts

# In[22]:


# Generate a bar plot showing the total number of measurements taken on each drug regimen using pandas
# Groupby Drug Regimen
drug_data = pd.DataFrame(combined_df.groupby(["Drug Regimen"]).count()).reset_index()

# drug_data
# configure df, axises for bar plot--> Needed assistance on set.index
drugs_df = drug_data[["Drug Regimen", "Mouse ID"]]
drugs_df = drugs_df.set_index("Drug Regimen")

# Bar Chart
drugs_df.plot(kind="bar", figsize=(10,3))

plt.title("Drug Treatment Count")
plt.show()
plt.tight_layout()


# In[29]:


# Generate a bar plot showing the total number of measurements taken on each drug regimen using pyplot.
drug_list = summary_df.index.tolist()
# drug_list

# drug count into list
drug_count = (combined_df.groupby(["Drug Regimen"])["Age_months"].count()).tolist()
#drug_count

# determine x axis--> per colleague
# x_axis = np.arange(len(drug_count))
x_axis = drug_list
plt.figure(figsize=(11,4))
plt.bar(x_axis, drug_count, color='b', alpha=0.5, align="center")

plt.title("Drug Treatment Count")
plt.xlabel("Drug Regimen")
plt.ylabel("Count")


# In[35]:


# Generate a pie plot showing the distribution of female versus male mice using pandas
gender_df = pd.DataFrame(combined_df.groupby(["Sex"]).count()).reset_index()
# gender_df.head()

gender_df = gender_df[["Sex","Mouse ID"]]
# gender_df.head()

# pie plot
plt.figure(figsize=(10,6))
ax1 = plt.subplot(121, aspect="equal")
gender_df.plot(kind="pie", y = "Mouse ID", ax=ax1, autopct='%1.1f%%',
              startangle=200, shadow=True, labels=gender_df["Sex"], legend = False, fontsize=14)

plt.title("Male & Female Mice Percentage")
plt.xlabel("")
plt.ylabel("")


# In[51]:


# Generate a pie plot showing the distribution of female versus male mice using pyplot
gender_count = (combined_df.groupby(["Sex"])["Age_months"].count()).tolist()
# gender_count

# labels
labels = ["Females", "Males"]
colors = ["red", "blue"]
explode = (0.1, 0)

# pie plot--> Help from colleague
plt.pie(gender_count, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=150)
plt.axis("equal")


# ## Quartiles, Outliers and Boxplots

# In[54]:


# Generate a box plot of the final tumor volume of each mouse across four regimens of interest
# Grouping by Regimen and Mouse ID
# Grouping by Regimen and Mouse ID
# Turn retrieved data into dataframe to easily manipulate
#Create a list to use as labels and dataframe

sorted_df = combined_df.sort_values(["Drug Regimen", "Mouse ID", "Timepoint"], ascending=True)
last_df = sorted_df.loc[sorted_df["Timepoint"] == 45]
last_df.head().reset_index()

# Capomulin
capomulin_df = last_df[last_df["Drug Regimen"].isin(["Capomulin"])]
capomulin_df.head().reset_index()

capomulin_obj = capomulin_df.sort_values(["Tumor Volume (mm3)"], ascending=True).reset_index()
capomulin_obj = capomulin_obj["Tumor Volume (mm3)"]
capomulin_obj

# quartiles
quartiles = capomulin_obj.quantile([.25,.5,.75])
lowerq = quartiles[0.25]
upperq = quartiles[0.75]
iqr = upperq - lowerq

# Generate a box plot of the final tumor volume of each mouse across four regimens of interest
fig1, ax1 = plt.subplots()
ax1.set_title("Final Tumor Volume in Capomulin Regimen")
ax1.set_ylabel("Final Tumor Volume (mm3)")
ax1.boxplot(capomulin_obj)
plt.show()


# In[45]:


# Put treatments into a list for for loop (and later for plot labels)


# Create empty list to fill with tumor vol data (for plotting)


# Calculate the IQR and quantitatively determine if there are any potential outliers. 

    
    # Locate the rows which contain mice on each drug and get the tumor volumes
    
    
    # add subset 
    
    
    # Determine outliers using upper and lower bounds
    


# In[46]:


# Generate a box plot of the final tumor volume of each mouse across four regimens of interest


# ## Line and Scatter Plots

# In[16]:


# Generate a line plot of tumor volume vs. time point for a mouse treated with Capomulin


# In[17]:


# Generate a scatter plot of average tumor volume vs. mouse weight for the Capomulin regimen


# ## Correlation and Regression

# In[18]:


# Calculate the correlation coefficient and linear regression model 
# for mouse weight and average tumor volume for the Capomulin regimen


# In[ ]:




