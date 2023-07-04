
partition = str(input(" What is your partition: "))

service = str(input(" What is your service: "))

region = str(input(" What is your location?: "))

accountid = int(input(" enter your account id "))

resourceid = int(input(" Enter your resource id "))

print("arn:" + str(partition) + ":" + str(service) + ":" + str(region) + ":" + str(accountid) + ":" + str(resourceid))

#sesssion 5 seperators  ---    use sep=':' to separate 