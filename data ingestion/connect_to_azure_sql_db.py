%python

df = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlserver://{servername:portname};databaseName={databasename};") \
    .option("dbtable", "{table_name}") \
    .option("user", "{username}") \
    .option("password", "{password}") \
    .load()

display(df)
