from getpass import getpass
import os
import replicate 
import replicate
from flask import Flask, render_template, request
from bs4 import BeautifulSoup 

REPLICATE_API_TOKEN = getpass()
os.environ["r8_DqBcjBRRLps5L3bsu7b2oNtfBZHsD7e3JJMEV"] = REPLICATE_API_TOKEN
app = Flask(__name__)

output = replicate.run(
  "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
  input={"prompt": "people having fuck"}
)
@app.route("/", methods=["GET", "POST"])
def generate_image():
    if request.method == "POST":
        gen = request.form["profile"]
        output = replicate.run(
            "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
            input={"prompt": gen}
        )
        soup = BeautifulSoup("<div id='pyImg'></div>", "html5")
        new_tag = soup.new_tag('img', src=output)
        soup.div.append(new_tag)
        print(output)
    return render_template("index.html")

print(output)


if __name__ == "__main__":
    app.run(debug=True)