from getpass import getpass
import os
import replicate 

REPLICATE_API_TOKEN = getpass()
os.environ["r8_DqBcjBRRLps5L3bsu7b2oNtfBZHsD7e3JJMEV"] = REPLICATE_API_TOKEN

output = replicate.run(
  "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
  input={"prompt": "people having fuck"}
)

print(output)