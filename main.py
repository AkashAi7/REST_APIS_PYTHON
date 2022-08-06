#program for the flask main file 


# GET retrieve data 
# POST submit new data
# PUT update 
# PATCH Partial Update 
# DELTE to delete the data 
 
from flask import Flask, jsonify, make_response , render_template,request

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"



# name="akash"
@app.route('/name')
def hello_name():
    return "Hello,akash!"

#Route for the web page
@app.route('/webpage')
def get_html():
    return render_template('index.html')


#Route for the query string 
@app.route('/query')
def get_query():
    if request.args:
     req=request.args
     return ''.join(f"{k}:{v} " for k,v in req.items())
    return "No query string"
    


# Flask get request 
# CRUD operation 

# This collection has single order entry 
order={
    "order1":{
        "size":"small",
        "toppings":"cheese",
        "crust":"thin"
    }
}


# Creating a Get method 
# Note that the default HTTP method is get do we don't need to specify the Get in the methods 


@app.route('/orders')
def get_orders():
    response=make_response(jsonify(order),200)
    return response 


if __name__=='__main__':
    app.run(debug=True)
