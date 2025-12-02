# AZURE + SPARK + DATABRICKS

## Azure Databricks Sales Outlet Data Transformation Project
### Project Overview
This project ingests sales outlet data stored in an Azure SQL Database, performs data transformation and cleansing using Azure Databricks, and finally stores the processed data in Azure Data Lake Storage (ADLS) in CSV format for business analytics use.

![Example Image](https://github.com/Niwedita-Kumari/data_engineering1/blob/main/DATA_TRANSFER.png)
### Key Steps
1. Connect to Azure SQL Database: Use Azure Databricks to establish a secure connection to the Azure SQL DB containing sales outlet data.

2. Data Cleaning and Transformation: Apply cleaning operations to handle missing values, duplicates, and inconsistencies in the data.

3. Data Insights Extraction: Analyze and generate insights such as top outlets by location, type, outlet size, and top-selling items by total sales.

4. Mount Azure Blob Storage: Mount the Azure Blob Storage or ADLS location onto Databricks for efficient data access.

5. Store Cleaned Data: Write the transformed and cleaned data from Databricks to the mounted storage location in CSV format for business consumption.

### Usage Instructions
1. Configure Databricks with access credentials to Azure SQL DB.

2. Run notebooks to load data, clean and transform it.

3. Perform analysis to extract business insights as required.

4. Mount the ADLS/Blob storage location using Databricks Utilities.

5. Save the final data as CSV in the mounted location.

### Technologies Used
+ Azure Databricks

+ Azure SQL Database

+ Azure Data Lake Storage (ADLS)/Azure Blob Storage

+ PySpark for data processing

### Conclusion
This setup enables a scalable, cloud-native pipeline for preparing sales data, making it readily available for business analytics in the desired CSV format.
