# command to mount the BLOB storage and save in the mount location

dbutils.fs.mount(
  source = "wasbs://{container}@{storage}.blob.core.windows.net",
  mount_point = "{mount_path}",
  extra_configs = {"fs.azure.account.key.{storage}.blob.core.windows.net": "{access_key}"}
)

df.write.options(header='True').csv("{mount_path}")
