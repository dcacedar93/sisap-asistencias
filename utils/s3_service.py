import boto3


class S3Client:
    def __init__(self, account_id="", bucket="", acl="public-read"):
        self.account_id = account_id
        self.bucket = bucket
        self.acl = acl
        self.client = self.get_client()
        self.get_bucket()
        self.bucket_url = f"https://{bucket}.s3.amazonaws.com"

    def get_client(self):
        return boto3.client("s3")

    def is_bucket_exits(self):
        response = self.client.list_buckets()
        list_buckets = response.get("Buckets", [])

        is_bucket_exits = list(
            filter(lambda bucket: bucket.get("Name") == self.bucket, list_buckets)
        )
        return is_bucket_exits

    def get_bucket(self):
        try:
            if not self.is_bucket_exits():
                self.client.create_bucket(ACL=self.acl, Bucket=self.bucket)
            else:
                print(f"El bucket {self.bucket} ya existe")
        except Exception as err:
            print(err)

    def list_objects(self):
        response = self.client.list_objects(Bucket=self.bucket)
        return response.get("Contents")

    def upload_file(self, path="", directory="", filename=""):
        try:
            bucket_filename = f"{directory}/{filename}"
            self.client.upload_file(path, self.bucket, bucket_filename)
            return filename
        except Exception:
            return False

    def upload_file2(self, path="", directory="", filename=""):
        try:
            bucket_filename = f"{directory}/{filename}"
            self.client.upload_file(path, self.bucket, bucket_filename)
            return f"{self.bucket_url}/{bucket_filename}"
        except Exception:
            return False

    def download_file(self, key="", filename="."):
        try:
            self.client.download_file(self.bucket, key, filename)
            return filename
        except Exception:
            return False

    def delete_bucket(self):
        try:
            if self.is_bucket_exits():
                self.client.delete_bucket(
                    Bucket=self.bucket, ExpectedBucketOwner=self.account_id
                )
                return True
            return False
        except Exception:
            return False

    def upload_fileobj(self, file, pathExtra=""):
        try:
            pathResource = f"{pathExtra}{file.filename}"
            self.client.upload_fileobj(
                file,
                self.bucket,
                pathResource,
                ExtraArgs={"ACL": self.acl, "ContentType": file.content_type},
            )
            return f"{self.bucket_url}/{pathResource}"
        except Exception:
            return False
