# QuickStart

1. Setup environment variable JWT token from pinata cloud. Download kaggle.json from kaggle.com and place it on your root directory. Make sure to verify you kaggle account.

2. Setups virtual environment

`
python3 -m venv .venv
source .venv/bin/activate

`

3. Install dependencies

`
pip install -r requirements
`

4. Start the server

`
python3 app.py
`

# Local Environment testing.

1. Enter your file URL and set GPU and TPU as true or false.
`
curl -X GET "http://localhost:3000/compute?fileUrl=<your_file_url>&enable_gpu=<true/false>&enable_tpu=<true/false>"
`
Output: folderID

2. Enter your folderID to check status of the compute   
`
curl -X GET "http://localhost:3000/status?folderID=<folderID>"
`
Output: Running/Complete

3. Enter your folderID to store compute output logs on IPFS CID
`
curl -X GET "http://localhost:3000/output?folderID=<folderID>"
`
Output: CID

4. Enter your CID on the URL to view the log
`
https://gateway.pinata.cloud/ipfs/<yourCIDhere>
`

# Example(On test API)

1. Enter your URL replacing sample URL
`
curl -X GET "https://kkpy.onrender.com/compute?fileUrl=https://raw.githubusercontent.com/madhukar123456/kaggle-kernel/main/python-code/mistraltest.ipynb&enable_gpu=true&enable_tpu=false"
`
Output: 
3dbbb8fa-e3eb-4948-80c1-8a071e1b55f8

2. Enter the folder ID to check status
`
curl -X GET "https://kkpy.onrender.com/status?folderID=3dbbb8fa-e3eb-4948-80c1-8a071e1b55f8"
`
Output:
Running
Output:
Complete

3. After you see output complete in few minutes, enter the folder ID to receive the CID

`
curl -X GET "https://kkpy.onrender.com/output?folderID=3dbbb8fa-e3eb-4948-80c1-8a071e1b55f8"
`

Output:
QmPDm74QL6kaToB2VEmcTwqRjk53GeqRFVwUhZno2pptQy

4. You can check your output log placing it on the URL as example below: 

`
https://gateway.pinata.cloud/ipfs/QmNhakdKbJyAVGJ4WmGBxJ3yfnrWAJ1HKk1Liksarzb4Ax
`