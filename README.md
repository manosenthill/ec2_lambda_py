# Working with EC2 using Python 

## Requirement
1. AWS account and credentials.
2. Python3
3. boto3


based on [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#client)

## IAM Permission
 lambda should have permission to transact with EC2. So add enough permission in IAM
  
 ![IAM_lambda_policy_permission](/docs/lambda_ec2_permission.png)
## Test

Start EC2
```
{
  "instances": "i-0c14c7b0022bc56fd",
  "action": "Start"
}
```
Stop EC2 Instances
```
{
  "instances": "i-0c14c7b0022bc56fd",
  "action": "Stop"
}
```
Reboot EC2 Instances
```
{
  "instances": "i-0c14c7b0022bc56fd",
  "action": "Reboot"
}
```
