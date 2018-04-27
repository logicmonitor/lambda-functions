## logicmonitor-send-cloudwatch-events
The 'logicmonitor-send-cloudwatch-events' Lambda function uses the LogicMonitor REST API to create LogicMonitor OpsNotes for CloudWatch Events. Once the Ops Notes have been created for monitored resources that have associated events, you'll see them on all graphs for those resources. 

## Overview
LogicMonitor® is the leading SaaS-based, performance monitoring platform for complex IT infrastructure. With coverage for thousands of technologies, LogicMonitor provides granular visibility into infrastructure and application performance. LogicMonitor Ops Notes are notes that display at a point in time on performance data graphs, and enable a visual eventstream. 

## Getting Started
Assuming you already have monitored AWS resources in LogicMonitor, you'll need to deploy the Lambda function in your AWS account (either via the AWS Serverless Application Repository or by uploading the zipped deployment package) and perform the following steps:

1. Provision LogicMonitor API Tokens that can be used to authenticate API requests:

    * Navigate to https://<your-account-name>.logicmonitor.com.

    * Locate the Users & Roles section within the Settings Page.

    * Identify an existing user or create a new existing user with permission to manage all devices. As a best practice, we recommend creating a designated API user for the integration.

    * Create a set of API Tokens from the Manage User dialog for the user in step 3. Copy the Access Id and Access Key values for use in the next section. 


2. Add your LogicMonitor API Tokens as Lambda environment variables:

    * Create or use an existing KMS Key - http://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html

    * Click the "Enable Encryption Helpers" checkbox

    * Paste the value of the Access Id in the API_ACCESS_ID environment variable and click encrypt.

    * Paste the value of the Access Key in the API_ACCESS_KEY environment variable and click encrypt.

    * Provide your LogicMonitor account name as the value of the ACCOUNT_NAME environment variable and click encrypt.
    

3. Configure CloudWatch Events Rules to be used as triggers for the Lambda Function:

    * Create a CloudWatch Event Rule that matches the events you'd like to show up in your LogicMonitor account - https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html

    * Add the rule as a trigger for this Lambda Function.


Note: This code requires the upload of a zip to include the "requests" library. Do no edit this in the lambda UI.

## More Information
For more information, see https://www.logicmonitor.com/support/lm-cloud/getting-started-lm-cloud/4-set-lm-clouds-custom-event-integrations/

