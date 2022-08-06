from flask import Flask, jsonify, make_response , render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
# Object seralization or deserialization 
from flask_marshmallow import Marshmallow



# Why do we need to import Marshmallow?
# Because we are going to use Marshmallow to serialize and deserialize our data.
# Marshmallow is a library that we can use to serialize and deserialize our data.
# We are using the RDMS (Relational Database Management System) to store our data.
# But the data is int the form of  the json 
# To convert the json to the structural format we are using the Marshmallow library.


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///myapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# Initialize the database
# inside that we have app instance
db=SQLAlchemy(app)

ma=Marshmallow(app)


# Defining the schema for the data

class MyAppSchema(ma.Schema):
    class Meta:
        fields=('orderid','size','topings','crust')



my_app_schema=MyAppSchema(many=True)
# creating table 

class Myapp(db.Model):
    orderid=db.Column(db.Integer,primary_key=True)
    size=db.Column(db.String(80),nullable=False)
    topings=db.Column(db.String(120),nullable=False)
    crust=db.Column(db.String(120),nullable=False)


@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/order', methods=['GET'])
def get_order():
    entries=Myapp.query.all()
    result=my_app_schema.dump(entries)
    return jsonify(result)
    # # Get all the orders
    # all_orders=Myapp.query.all()
    # # Serialize the data
    # schema=MyAppSchema(many=True)
    # data=schema.dump(all_orders)
    # return jsonify(data)


# Post request using sqlalchemy 
# Myapp is table name 
# orderid size ,topinfgs and crust are the columns of the table 

@app.route('/order', methods=['POST'])
def post_add_order():
    req=request.get_json()
    orderid=req['orderid']
    size=req['size']
    topings=req['topings']
    crust=req['crust']
    new_order=Myapp(orderid=orderid,size=size,topings=topings,crust=crust)
    db.session.add(new_order)
    db.session.commit()
    # redirect to the  get method
    return redirect(url_for('get_order'))



# Delete request using sqlalchemy
# We will be taking the orderid as the parameter
# and deleting the order based on the orderid
# We will be using the delete method of the sqlalchemy

@app.route('/order/<orderid>', methods=['DELETE'])
def delete_order(orderid):
    order=Myapp.query.get(orderid)
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for('get_order'))




# Put request using sqlalchemy
# We will be taking the orderid as the parameter
# and updating the order based on the orderid
# We will be using the update method of the sqlalchemy

@app.route('/order/<orderid>', methods=['PUT'])
def update_order(orderid):
    req=request.get_json()
    order=Myapp.query.get(orderid)
    order.size=req['size']
    order.topings=req['topings']
    order.crust=req['crust']
    db.session.commit()
    return redirect(url_for('get_order'))
    
if __name__=='__main__':
    # Craete database and table 
    db.create_all()
    app.run(debug=True)

    
