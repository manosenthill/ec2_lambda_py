import json
import boto3

ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    instances=event["instances"].split(',')
    action=event["action"]
    
    if action=="Start":
        response=ec2.start_instances(InstanceIds=instances)
    elif action=="Stop":
        response=ec2.stop_instances(InstanceIds=instances)
    elif action=="Reboot":
        response=ec2.reboot_instances(InstanceIds=instances)
    print(response)
    
