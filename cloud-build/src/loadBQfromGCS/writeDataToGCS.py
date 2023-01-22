from faker import Faker
from google.cloud import storage
import datetime

def writeDataToGCS(PROJECT_ID,BUCKET):
    #Initialize few variables
    storage_client 	= storage.Client(project=PROJECT_ID)
    fake   			= Faker()
    bucket 			= storage_client.bucket(bucket_name=BUCKET)
    blob   			= bucket.blob('feature-store-data/cc_data.csv')

    #Get the user input for # of rows to be created
    #num_rows = int(input('How many rows you want to create? : '))
    num_rows = 10000
    print('The number of rows to be created are : ',str(num_rows))
    #Creating the Synthetic Data and Storing it in the GCS Bucket
    with blob.open(mode='w') as fl:
        print("Start Time is : ",datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"))
        for n in range(num_rows):
            if n==0:
                header = 'cc_num,cust_num,credit_limit,zip_code,cash_back_pct,ftr_dttm\n'
                fl.write(header)
            else:
                cc_num        = fake.credit_card_number()
                cust_num      = fake.uuid4()
                credit_limit  = fake.numerify(text='%#000')
                zip_code      = fake.zipcode()
                cash_back_pct = fake.numerify(text='%.#')
                ftr_dttm      = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
                cc_row        = cc_num+','+cust_num+','+credit_limit+','+zip_code+','+cash_back_pct+','+ftr_dttm+'\n'
                #print(cc_row)
                fl.write(cc_row)
        print("End Time is : ",datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"))