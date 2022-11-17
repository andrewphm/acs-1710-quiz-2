from flask import Flask, request, render_template
import requests
import json



URL = "https://swapi.py4e.com/api/"
app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    category = request.args.get('category')
    id = request.args.get("id")


    if id and category:
        response = requests.get(f'{URL}{category}/{id}')
        result = json.loads(response.content)
        for i in list(result):
            key_str = str(i).replace("_", " ")
            result[key_str] = result.pop(i)

        context = {"result": result}
        return render_template("home.html", **context)
    else:
        return render_template("home.html")    





if __name__ == "__main__":
    app.run(debug=True)
