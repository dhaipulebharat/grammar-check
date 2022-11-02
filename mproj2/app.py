from flask import Flask,render_template,request,jsonify,request,redirect,url_for

from gram import get_response

app=Flask(__name__)

@app.route("/")
def Welcome():
    return render_template("base.html")
@app.route("/success/<string:msg>")
def success(msg):
    return render_template("result.html",output=msg)

@app.route("/predict",methods=["GET","POST"])
def predict():
    unchck_ms=""
    if request.method=="POST":
        message=request.form['msg']
        response= get_response(message)
    return redirect(url_for("success",msg=response))

if __name__ == "__main__":
    app.run(debug=True)





""" text=request.get_json().get("message")
    # TODO:check if text is valid
    response= get_response(text)
    message={"answer":response}
    return jsonify(message) """