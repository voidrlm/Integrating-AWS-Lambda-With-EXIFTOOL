import json
import boto3
import logging
import subprocess
import os
import re

# Set up a logger for logging information and errors
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create an S3 client using the AWS SDK for Python (Boto3)
s3 = boto3.client('s3')

# Specify the S3 bucket name where your media files are stored
bucket_name = ''  # Replace with your actual bucket name

# AWS Lambda function handler


def lambda_handler(event, context):
    try:
        # Retrieve the request body from the event
        request_body = event

        # Extract the file name from the request body
        fileName = request_body.get('fileName', '')

        # Define a temporary path on the Lambda instance for file processing
        tempPath = "/tmp/" + fileName

        # Download the requested file from the S3 bucket to the Lambda instance
        s3.download_file(bucket_name, 'media/' + fileName, tempPath)

        # Extract EXIF (Exchangeable image file format) metadata from the downloaded file
        metaData = extractEXIFData(tempPath)

        # Remove the temporary file from the Lambda instance
        os.remove(tempPath)

        # Prepare a response with HTTP status code 200 (OK) and the extracted metadata
        response = {
            'statusCode': 200,
            'body': json.dumps(metaData)
        }

    except Exception as e:
        # Handle exceptions and prepare an error response with HTTP status code 500 (Server Error)
        response = {
            'statusCode': 500,
            'body': json.dumps('Error: ' + str(e))
        }

    # Return the response to the caller
    return response

# Method to extract EXIF data from a media file using the ExifTool


def extractEXIFData(mediaFilePath):
    # Define a command to run ExifTool and extract JSON-formatted metadata from the file
    command = "/opt/bin/perl /opt/bin/exiftool -json " + mediaFilePath

    # Execute the command and capture the standard output
    completed_process = subprocess.run(
        command, stdout=subprocess.PIPE, shell=True, text=True)

    # Check for errors in the command execution
    if completed_process.returncode == 0:
        # If successful, parse the JSON output and log it
        json_output = completed_process.stdout
        data = json.loads(json_output)
        logger.info(data)
        return data
    else:
        # If there are errors, return an empty dictionary
        return {}
