# -*- coding: utf-8 -*-
# Minio Python Library for Amazon S3 Compatible Cloud Storage.
# Copyright (C) 2016 Minio, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Note: YOUR-ACCESSKEYID, YOUR-SECRETACCESSKEY, my-testfile, my-bucketname and
# my-objectname are dummy values, please replace them with original values.

from minio import Minio

client = Minio('play.minio.io:9000',
               access_key='Q3AM3UQ867SPQQA43P2F',
               secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG')

# Put a file with default content-type.
events = client.listen_bucket_notification('my-bucket', 'my-prefix/',
                                           '.my-suffix',
                                           ['s3:ObjectCreated:*',
                                            's3:ObjectRemoved:*'])
for event in events:
    print(event)
