"""
Ticket EWOK-303
AWS clean up: deleting everything from the S3 buckets that contains user-level data and is older than 24 months
"""
import datetime
import csv
import boto  #AWS library
from fnmatch import fnmatch # Unix filename pattern matching
from boto.s3.key import Key

def delete_from_s3(bucket_name, file_name):
    conn = boto.connect_s3()
    bucket = conn.get_bucket(bucket_name)
    # Get the Key object of the bucket:
    k = Key(bucket)
    # Create a new key with id as the name of the file:
    k.key = file_name
    # Delete the file
    #bucket.delete_key(k)

def selecting_all_files(bucket_name,file_format, date_to_delete):
    # List all files in the folder
    conn = boto.connect_s3()
    bucket = conn.get_bucket(bucket_name)
    all_file_names = list(bucket.list('', '/'))
    all_matching_names = []
    for single_file in all_file_names:
        if fnmatch(single_file.name, date_to_delete.strftime(file_format)) == True:
            all_matching_names.append(single_file.name)
    return all_matching_names


date_today = datetime.date.today()
date_to_delete_from =  date_today - datetime.timedelta(days=4*365) #datetime.date(2016, 01, 01)
date_to_delete_up_to = date_today - datetime.timedelta(days=2*365) #datetime.date(2016, 01, 04)
delta_number_days = date_to_delete_up_to - date_to_delete_from

dates_to_delete= list((date_to_delete_from + datetime.timedelta(n) for n in range(delta_number_days.days)))

with open('bucket_info.csv', mode='r') as bucket_info:
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
            if '*' in file_format:
                file_names = selecting_all_files(bucket_name, file_format, date_to_delete)
                for file_name in file_names:
                    print (bucket_name + folder_name + '/' + file_name)
                    #delete_from_s3(bucket_name, file_name)
            else:
                file_name = folder_name + '/' + date_to_delete.strftime(file_format) # This works if on the file we use a different format...
                print (bucket_name + '/' + folder_name + '/' + file_name)
                # delete_from_s3(bucket_name, file_name)
            #print ('Deleted file (in case it exists): ' + bucket_name + '/' + file_name)