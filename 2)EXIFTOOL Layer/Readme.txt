You can easily create your own AWS Lambda layer for the latest EXIFTOOL using the provided shell script below.
I've already generated an Exiftool layer that's available in the folder.
Feel free to use this layer as needed for your Lambda functions.


How to add this layer to your lambda function

Upload the Layer ZIP File:

To upload the ZIP file to AWS Lambda, follow these steps:

a. Sign in to the AWS Management Console.

b. Go to the AWS Lambda service.

c. Select the Lambda function to which you want to add the layer.

d. In the "Function code" section, scroll down to the "Layers" box.

e. Click on "Add a layer."

f. Choose "Upload a .zip file" option.

g. Click on the "Upload" button and select the ZIP file containing your Layer code.

h. Click "Add" to upload the ZIP file.

Save Changes:

After you've added the Layer ZIP file, don't forget to save the Lambda function configuration by clicking the "Save" button at the top of the page.

Grant Permissions (if necessary):

Ensure that your Lambda function has the necessary IAM (Identity and Access Management) permissions to access the Layer.
You may need to modify the function's execution role to include the necessary permissions.