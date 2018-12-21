import json
import re
import boto3
import threading
from multiprocessing import Process, Pipe
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2', region_name='REGION HERE')

def volume_exists(snap_id, volume_id):
    try:
        ec2.describe_volumes(VolumeIds=[volume_id])
        return True
    except ClientError:
        # create tag for orphaned snapshot
        ec2.create_tags(
            Resources=[
                snap_id,
            ],
            Tags=[
                {'Key': 'orphaned', 'Value': 'true'}
            ]
        )
        print snap_id
        return False

def lambda_handler(event, context):
    threads = []

    # get all the snapshots
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    
    # check which snapshot is orphaned
    for s in snapshots:
        a = Process(target=volume_exists, args = (s['SnapshotId'], s['VolumeId']))
        threads.append(a)
        a.start()
    
    for x in threads:
        x.join()
