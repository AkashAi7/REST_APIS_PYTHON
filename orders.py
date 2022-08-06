#program for the flask main file 


# GET retrieve data 
# POST submit new data
# PUT update 
# PATCH Partial Update 
# DELTE to delete the data 
 
from urllib import response
from flask import Flask, jsonify, make_response , render_template,request

app1=Flask(__name__)

@app1.route('/')
def hello_world():
    return "Hello, World!"



# name="akash"
@app1.route('/name')
def hello_name():
    return "Hello,akash!"

#Route for the web page
@app1.route('/webpage')
def get_html():
    return render_template('index.html')


#Route for the query string 
@app1.route('/query')
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
    ,
       "order2":{
        "size":"medium",
        "toppings":"olive",
        "crust":"thick"
    }
}


# Creating a Get method 
# Note that the default HTTP method is get do we don't need to specify the Get in the methods 

# Shows or displays the collection to the user on the browser tab 
# @app1.route('/orders', methods=['GET'])
@app1.route('/orders')
def get_orders():
    response=make_response(jsonify(order),200)
    return response 


# Get method with order id
@app1.route("/orders/<order_id>")
def get_order(order_id):
    if order_id in order:
        return jsonify(order[order_id])
    return jsonify({"error":"order not found"}),404


# Selecting the order based on the intern response of the order like size or crust or toppings



@app1.route("/orders/<order_id>/<items>")
def get_item(order_id,items):
    item=order[order_id]
    if  item:
        response=make_response(jsonify(item),200)
        return response
    return jsonify({"error":"order not found"}),404



# Post methods for adding new data
@app1.route("/orders/<orderid>",methods=['POST'])
def post_order(orderid):
    req=request.get_json()
    if orderid in order:
        response=make_response(jsonify({"error":"order already exists"}),200)
        return response
    order.update({orderid:req})
    response=make_response(jsonify({"success":"order added"}),201)
    return response

# For testing post request on the postman


# Post method must be selected then in the body section 
# the data must be added in the body section
# the head of the json must be avoided  example 
#    {
#     "size":"small",
#     "toppings":"cheese",
#     "crust":"thin"
#     }





# Put method for updating the data

# If the value already exists then we can update the value
# If the value does not exist then we can add the value

@app1.route("/orders/<orderid>",methods=['PUT'])
def update_order(orderid):
    req=request.get_json()
    if orderid in order:
        order[orderid]=req
        response=make_response(jsonify({"message":"order updated "}),200)
        return response
    order[orderid]=req
    response=make_response(jsonify({"success":"New order added"}),201)
    return response



# Patch method for partial update
# In put the value is checked if the value exists or not if it does not exits then the value is added
# on the other habd the patch method is just update method 

@app1.route("/orders/<orderid>",methods=['PATCH'])
def update_patch_order(orderid):
    req=request.get_json()
    if orderid in order:
        for k,v in req.items():
            order[orderid][k]=v
        response=make_response(jsonify({"message":"order updated "}),200)
        return response
    order[orderid]=req
    response=make_response(jsonify({"success":"New order added"}),201)
    return response




if __name__=='__main__':
    app1.run(debug=True)
