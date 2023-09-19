#!/usr/bin/env python3

import weaviate
from dotenv import load_dotenv
import os

load_dotenv(".env")

auth_config = weaviate.AuthApiKey(api_key=os.getenv('WEAVIATE_ADMIN_KEY'))
client = weaviate.Client(url=os.getenv('WEAVIATE_CLUSTER_URL'),auth_client_secret=auth_config)

print(client.schema.get())
