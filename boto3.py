import boto3
ec2 = boto3.client('ec2')

# Create the instance
# response = ec2.run_instances(
#     ImageId='ami-0a695f0d95cefc163',
#     InstanceType='t2.micro',
#     MinCount=1,
#     MaxCount=1,
#     KeyName='linux-python',
#     SecurityGroupIds=['sg-039cd7ecc26cd9b7a'],
#     SubnetId='subnet-04715334606a844ca',
#     TagSpecifications=[
#         {
#             'ResourceType': 'instance',
#             'Tags': [
#                 {
#                     'Key': 'Name',
#                     'Value':'Giftstore'
#                 },
#             ]
#         },
#     ]
# )

# Print the instance ID
#print(response['Instances'][0]['InstanceId'])
