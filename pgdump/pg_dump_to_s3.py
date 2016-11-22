import subprocess as sub
from datetime import datetime
import os
import gzip
os.environ['PGPASSWORD']='db-password-here'
class pg_dump(object):
    def __init__(self,host,user,db,bucket):
               self.host=host
               self.user=user
               self.db=db
               self.file_name=''
               self.bucket=bucket
               self.path='/tmp'
    def cur_date_time(self):
           date_obj=datetime.now().strftime('%Y%m%d%H%M%S')
           return date_obj

    def db_dump(self):
           self.file_name=self.db+'.sql-'+self.cur_date_time()
           args=['pg_dump','-h',self.host,'-U',self.user,'-f',self.file_name,self.db]
           os.chdir(self.path)
           p=sub.call(args)
           self.convert_to_gz(self.file_name)
           self.file_name=self.file_name+'.gz'
           self.copy_dump_to_s3(self.file_name,self.bucket)
           os.remove(self.file_name)
    def convert_to_gz(self,file):
         args=['gzip',file]
         sub.call(args)
    def copy_dump_to_s3(self,f,b):
          cmd=['/usr/local/bin/aws','s3','cp',f,b]
          sub.call(cmd)
