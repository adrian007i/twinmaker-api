import boto3
import datetime 
import time


# AWS SiteWise Alias
alias = '/biofilm/led/status'
 
# Create a Boto3 SiteWise client
client = boto3.client('iotsitewise', region_name='us-east-1', aws_access_key_id="",aws_secret_access_key="" )

def update_sitewise(status):
    date_time = int(time.time()) 
    led_light_status = status    #modify this line to set the led_light_status

    # Create the JSON payload
    payload = {
        "entries": [
            {
                "entryId": str(date_time),
                "propertyAlias": alias,
                "propertyValues": [
                    {
                        "value": {
                            "booleanValue":  led_light_status
                        },
                        "timestamp": {
                            "timeInSeconds": date_time
                        },
                        "quality": "GOOD"
                    }
                ]
            }
        ]
    }


    # Send the data to AWS SiteWise
    try:
        client.batch_put_asset_property_value(entries=payload['entries'])
    except Exception as e:
        print("Error sending data: {}".format(e))

