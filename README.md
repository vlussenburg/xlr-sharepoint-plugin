# xlr-sharepoint-plugin

Alpha workspace

![shared-configuration](images/shared-configuration.png)

# Testing
This readme assumes familiarity with Amazon EC2. Now, it's possibly that you haven't spun up Amazon EC2 instance before. Go educate yourself and spin up a random Windows box and connect to it so you know how to work Amazon. There's beautiful guide on the interwebz, just Google It (c).

Spin up this AMI in Amazon EC2: ````Windows_Server-2008-R2_SP1-English-64Bit-SharePoint_2010_SP2_Foundation-2018.11.29 (ami-12029d68)````. Note that the exact AMI ID and description can change, but the important part is that it's SharePoint 2010 (which is the target SharePoint version of this plugin rn).

Add a inbound rule allowing your IP to connect to port 80 (http). Since the SharePoint version might have vulnerablities, I recommend against exposing this image to the whole big bad internet.

Log in using basic authentication using the Administrator account. Voila, Bob's your uncle.