#%%
length = 1000000


table_name = "t"
sql = f"split table {table_name} by "
for i in range(1,length):
	sql = sql + f"({i}), "
sql = sql[:-2]
sql = sql + ";"
f = open("split_one_sql.sql", "w")
f.write(sql)
f.close()
# %%
# -9223372036854775808  9223372036854775807
# 1000 * 1000 = 100 000
table_name = "tm"
with open("1000.sql","r") as f:
	lines = f.readlines()
sqls = []
for line in lines:
	sql =  f"split table {table_name} between ({line[22:42]}) AND ({line[53:73]}) REGIONS 1000;"
	sqls.append(sql)
with open("split_1000.sql","w") as f:
	for sql in sqls:
		f.write(sql+"\n")

# %%

# %%
# -9223372036854775808  9223372036854775807
# 1000 * 1000 = 100 000
table_name = "tz"
with open("1000.sql","r") as f:
	lines = f.readlines()
sqls = []
for line in lines:
	sql =  f"split table {table_name} between ({line[22:42]}) AND ({line[53:73]}) REGIONS 10;"
	sqls.append(sql)
with open("split_1000_10.sql","w") as f:
	for sql in sqls:
		f.write(sql+"\n")

# %%
