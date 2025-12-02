# Databricks notebook source

# COMMAND to replace all null values in Outlet_size with High ----------

df = df.na.fill({'Outlet_Size': 'High'})
display(df)

# COMMAND to replace all null values in Outlet_Location_Type with Tier3----------

df = df.na.fill({'Outlet_Location_Type': 'Tier3'})
display(df)

# COMMAND to replace all LF values in Item_Fat_Content with Low Fat----------

df=df.replace('LF','Low Fat','Item_Fat_Content')
display(df)
