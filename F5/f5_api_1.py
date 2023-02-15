from f5.bigip import ManagementRoot

# Connect to the BigIP
mgmt = ManagementRoot("10.100.115.100", "admin", "eve")


#Delete a pool if it exists
if mgmt.tm.ltm.pools.pool.exists(name='mypool', partition='Common'):
    pool_b = mgmt.tm.ltm.pools.pool.load(name='mypool', partition='Common')
    pool_b.delete()


# Create a new pool on the BIG-IP
mypool = mgmt.tm.ltm.pools.pool.create(name='mypool', partition='Common')

# Load an existing pool and update its description
pool_a = mgmt.tm.ltm.pools.pool.load(name='mypool', partition='Common')
pool_a.description = "New description"
pool_a.update()


# Get a list of all pools on the BigIP and print their names and their
# members' names
pools = mgmt.tm.ltm.pools.get_collection()
for pool in pools:
    print(pool.name)
    for member in pool.members_s.get_collection():
         print(member.name)
