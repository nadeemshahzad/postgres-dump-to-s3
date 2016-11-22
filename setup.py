from setuptools import setup

setup(name='pgdump',
      version='0.1',
      description='PostgreSQL dump to s3',
      author='Nadeem Shahzad',
      author_email='nadeem.shahzad@arbisoft.com',
      packages=['pgdump'],
      scripts=['pg_dump_to_s3'])
