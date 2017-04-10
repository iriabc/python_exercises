"""
EWOK ticket: https://essencedigital.atlassian.net/browse/EWOK-303
AWS clean up: deleting everything from the S3 buckets that contains user-level data and is older than 24 months
"""
import datetime
import boto  #AWS library
from boto.s3.key import Key

def delete_from_s3(bucket_name, file_name):
    conn = boto.connect_s3()
    bucket = conn.get_bucket(bucket_name)
    # Get the Key object of the bucket
    k = Key(bucket)
    # Create a new key with id as the name of the file
    k.key = file_name
    # Delete the file
    bucket.delete_key(k)


# Test 1: Trying to delete this: s3://ewok-303-dev-test/data.log
delete_from_s3("ewok-303-dev-test", "data.log")

# Test 2: Trying to delete this: s3://ewok-303-dev-test/dt=12-27-2015.log
bucket_name = "ewok-303-dev-test"
date_to_delete = "12-27-2015"
file_name = "dt=" + date_to_delete + ".log"

delete_from_s3(bucket_name, file_name)

# Test 3: Trying to delete s3://ewok-303-dev-test/dt=12-27-2015
bucket_name = "ewok-303-dev-test"
date_to_delete = datetime.date(2015, 12, 27).strftime("%m-%d-%Y")
file_name = "dt=" + str(date_to_delete) + ".log"

delete_from_s3(bucket_name, file_name)
print ("Deleted file: " + file_name)


# Test 4
bucket_name = 'ewok-303-dev-test'
folders_and_formats = {'/iso_dashes'}
folders_name = ['/iso_dashes', '/usa_dashes']
date_formats = ["%Y-%m-%d", "%m-%d-%Y", "%Y%m%d"] #Too manual,I would like to change it
date_today = datetime.date.today()
# date_to_delete_from = date_today - datetime.timedelta(days=4*365)
# date_to_delete_up_to = date_today - datetime.timedelta(days=2*365)
#import pdb; pdb.set_trace()
date_to_delete_from = datetime.date(2015, 01, 01)
date_to_delete_up_to = datetime.date(2015, 01, 24)
delta_number_days = date_to_delete_up_to - date_to_delete_from

dates_to_delete= list((date_to_delete_from + datetime.timedelta(n) for n in range(delta_number_days.days)))

for folder_name in folders_name:
    for date_format in date_formats:
        for date_to_delete in dates_to_delete:
            file_name = folder_name + '/dt=' + date_to_delete.strftime(date_format)
            delete_from_s3(bucket_name, file_name)
            print ("Deleted file: " + bucket_name + file_name)


# Test 5
dates_to_delete= list((date_to_delete_from + datetime.timedelta(n) for n in range(delta_number_days.days)))

with open('bucket_info_test.csv', mode='r') as bucket_info:
    reader = csv.reader(bucket_info)
    next(reader, None)  # Skip the header
    for row in reader:
        bucket_name = row[0]
        folder_name = row[1]
        file_format = row[2] # What we are expecting 'YYYY-MM-DD'
        file_format = file_format.replace('YYYY', '%Y')
        file_format = file_format.replace('MM', '%m')
        file_format = file_format.replace('DD', '%d')

        for date_to_delete in dates_to_delete:
            file_name = folder_name + '/' + date_to_delete.strftime(file_format) # This works if on the file we use a different format...
            get
            print file_name
            delete_from_s3(bucket_name, file_name)
            print ('Deleted file (in case it exists): ' + bucket_name + '/' + file_name)