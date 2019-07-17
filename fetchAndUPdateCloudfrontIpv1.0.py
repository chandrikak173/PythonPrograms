import urllib.request, json
import boto3,re
import os
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    #def lambda_handler(event, context):
    # TODO implement
    #a=sum()
    return {
        'statusCode': 200,
        'body': json.dumps('CLOUDFRONT Service Update Report'),
        'checkService': checkService()
    }

### The function writetoS3() writes updated ip-ranges.json file to S3 ###

def writetoS3():
    url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    bucket_name = "cloudfronservice"
    file_name = "ip-ranges.json"
    s3_path = file_name
    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=json.dumps(data))

### The function readDataFromS3() reads ip-ranges.json file from S3 ###

def readDataFromS3():
    s3IP=[]
    #oldCount=0
    bucket_name = "cloudfronservice"
    file_name = "ip-ranges.json"
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_name, file_name)
    s3Data = obj.get()['Body'].read()
    s3Data = json.loads(s3Data)    
    for i in s3Data['prefixes']:
        if i['service'] == 'CLOUDFRONT':
            s3IP.append(i['ip_prefix'])         
    for i in s3Data['ipv6_prefixes']:
        if i['service'] == 'CLOUDFRONT':
            s3IP.append(i['ipv6_prefix'])
    return s3IP

### The function checkService() compares ip-ranges.json file to S3 and URL and checks whether the CLOUDFRON Service IPs have been updated ###

def checkService():
    urlData = urllib.request.urlopen("https://ip-ranges.amazonaws.com/ip-ranges.json")
    newData = json.loads(urlData.read())
    s3IP=readDataFromS3()
    urlIP=[]
    for i in newData['ipv6_prefixes']:
        if i['service'] == 'CLOUDFRONT':
            urlIP.append(i['ipv6_prefix'])
    for i in newData['prefixes']:
        if i['service'] == 'CLOUDFRONT':
            urlIP.append(i['ip_prefix'])
    ipToBeAdded=list(set(urlIP) - set(s3IP))
    ipToBeDeleted=list(set(s3IP) - set(urlIP))
    print("ipToBeAdded"+str(len(ipToBeAdded)))
    print("ipToBeAdded"+str(len(ipToBeDeleted)))
    if len(ipToBeAdded) == 0 and len(ipToBeDeleted)==0:
        return "The CLOUDFRONT Service is not updated"
    else:
        updateSecurityGroup(ipToBeAdded,ipToBeDeleted)
        message="Hello Team,\n\n" +"IP which have been deleted from ip-ranges.json:\t" + str(ipToBeDeleted) +"\nIP which have been added to ip-ranges.json:\t"+  str(ipToBeAdded)
        client = boto3.client('sns')
        response = client.publish(
        TopicArn='arn:aws:sns:us-west-2:439167469925:demoSNS',Subject="Data in ip-ranges.json has been updated",  
        Message=message
        )
        print ("Response: {}".format(response))  
        print("message published")
        writetoS3() 
        
### The function adds and/or removes the rules of security group ###        

def updateSecurityGroup(ipToBeAdded,ipToBeDeleted):
    ruleMaxLimit=30
    ec2 = boto3.client('ec2')
    #ipInSecurityRule=[getCountOfRules()]
    ipAdded=ipToBeAdded            #['52.124.128.0/17','2406:da12::/36','54.230.0.0/16','2404:c2c0:8000::/36']
    ipRemoved=ipToBeDeleted
    print("IPAdded")
    print(ipAdded)
    print("IPRemoved")
    print(ipRemoved)
    updateSecurityRules=os.environ['updateSecurityRules']
    security_group_ids=os.environ['securityGroupId']
    security_group_ids=security_group_ids.split(',')
    #print(updateSecurityGroup)
    for security_group in security_group_ids:
        ipInSecurityRule=getCountOfRules(security_group)
        print("ipInSecurityRule"+str(ipInSecurityRule))
        countOfSecurityRules=len(ipInSecurityRule)
        print("count of security rules in" + security_group +" "+ str(countOfSecurityRules))
        if countOfSecurityRules < ruleMaxLimit: #and ruleMaxLimit-countOfSecurityRules <= len(ipAdded):
            security_group_id=security_group
            break
        else:
            message="Hello Team,\n\n" + "Maximum rule limit has reached. The current count of rules in Security Group "+ security_group + "is: " + str(countOfSecurityRules)
            client = boto3.client('sns')
            response = client.publish(
            TopicArn='arn:aws:sns:us-west-2:439167469925:demoSNS',Subject="Alert: Security Maximum Limit Has Reached",  
            Message=message
            )
            print ("Response: {}".format(response))  
            print("message published")
            #return "Maximum rule limit has reached. The current count of rules in Security Group "+ security_group + "is: " + str(countOfSecurityRules)
            continue
    print("Security Group ID" + security_group_id)       
    if updateSecurityRules.lower() == "true":
        print("True")
        try:
            if len(ipAdded) != 0:
                for ip in ipAdded:
                    if ip.find(".") == -1:
                        print("ipv6 "+ip)
                        addIPv6 = ec2.authorize_security_group_ingress(
                            GroupId=security_group_id,
                            IpPermissions=[
                                {'IpProtocol': 'tcp',
                                 'FromPort': 443,
                                 'ToPort': 443,
                                 'Ipv6Ranges': [{'CidrIpv6': ip}]},
                            ])
                    elif ip.find(":") == -1:
                        print("ipv4 "+ip)
                        addIPv6 = ec2.authorize_security_group_ingress(
                            GroupId=security_group_id,
                            IpPermissions=[
                                {'IpProtocol': 'tcp',
                                 'FromPort': 443,
                                 'ToPort': 443,
                                 'IpRanges': [{'CidrIp': ip}]},
                            ])
            if len(ipRemoved) != 0:
                for ip in ipRemoved:
                    if ip.find(".") == -1:
                        print("ipv6 "+ip)
                        addIPv6 = ec2.revoke_security_group_ingress(
                            GroupId=security_group_id,
                            IpPermissions=[
                                {'IpProtocol': 'tcp',
                                 'FromPort': 443,
                                 'ToPort': 443,
                                 'Ipv6Ranges': [{'CidrIpv6': ip}]},
                            ])
                    elif ip.find(":") == -1:
                        print("ipv4 "+ip)
                        addIPv6 = ec2.revoke_security_group_ingress(
                            GroupId=security_group_id,
                            IpPermissions=[
                                {'IpProtocol': 'tcp',
                                 'FromPort': 443,
                                 'ToPort': 443,
                                 'IpRanges': [{'CidrIp': ip}]},
                            ])
        except ClientError as e:
            print(e)
        except TypeError as e:
            ptint(e)
        except Exception as e:
            print(e)
            

    else:
        print("Not updated")

### The function gets the list of IPs in the security group ###


def getCountOfRules(security_group_id):
    #security_group_ids = os.environ['securityGroupId']
    #security_group_ids=security_group_ids.split(",")
    ec2 = boto3.client('ec2')
    ipInSecurityRule=[]
    response = ec2.describe_security_groups(GroupIds=[security_group_id])
    for i in response['SecurityGroups']:
       for j in i['IpPermissions']:        
           try:
              for k in j['IpRanges']:
                  print("IP Ranges: "+k['CidrIp'])
                  ipInSecurityRule.append(k['CidrIp'])
           except Exception:
              print("No value for ports and ip ranges available for this security group")
              continue   
    for i in response['SecurityGroups']:
       for j in i['IpPermissions']:        
           try:
              for k in j['Ipv6Ranges']:
                  print("IPv6 Ranges: "+k['CidrIpv6'])
                  ipInSecurityRule.append(k['CidrIpv6'])
           except Exception:
              print("No value for ports and ipv6 ranges available for this security group")
              continue   
    #return len(ipInSecurityRule)
    return ipInSecurityRule      