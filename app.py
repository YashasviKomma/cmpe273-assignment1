from flask import Flask
from github import Github
import sys,yaml,json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"
@app.route('/v1/<filename>')
def gitintegration(filename):
    print filename
    y=Github("yashasvi.komma@sjsu.edu","")
    print sys.argv
    string = sys.argv[1]
    print string
    words = string.split("/")
    print words
    repo = words[len(words) - 1]
    print repo
    user=y.get_user()
    grepo=user.get_repo(repo)
    filelist=filename.split(".")
    if filelist[len(filelist) - 1] == "yml":
        ymlfile = grepo.get_file_contents(filename)
        return yaml.dump(yaml.load(ymlfile.decoded_content))
    elif filelist[len(filelist) - 1] == "json":
        jsonfile = grepo.get_file_contents(filelist[0] + ".yml")
        return json.dumps(yaml.load(jsonfile.decoded_content), sort_keys=True, indent=2)
    else:
        return "Provide the extension type"
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
