import mysql.connector
import os
import base64
import Constants
cnx = None

def get_connection():
    global cnx

    if not cnx:
        try:
            cnx = mysql.connector.connect(user=Constants.LOCAL_DATABASE_USER,
                                          password=Constants.LOCAL_DATABASE_PASSWORD,
                                          host=Constants.LOCAL_DATABASE_ENDPOINT,
                                          database=Constants.LOCAL_DATABASE_NAME,
                                          auth_plugin='mysql_native_password')
        except:
            cnx = mysql.connector.connect(user=Constants.PRODUCTION_DATABASE_USER,
                                          password=Constants.PRODUCTION_DATABASE_PASSWORD,
                                          host=Constants.PRODUCTION_DATABASE_ENDPOINT,
                                          database=Constants.PRODUCTION_DATABASE_NAME,
                                          auth_plugin='mysql_native_password')
        cnx.autocommit = True
    return cnx

def get_categories():
    cursor = get_connection().cursor()
    cursor.execute("SELECT category_name FROM category")
    rows = cursor.fetchall()

    result = []

    for row in rows:
        result.append(row[0])
    return result

def add_product(image, body):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "Insert into products (category_name, email, product_name," \
          " description, price, available_quantity, image) values (%s,%s,%s,%s,%s,%s,%s)"
    values = (body['category_name'], body['email'], body['product_name'],
              body['description'], body['price'], body['available_quantity'], base64.b64encode(image))
    rows = cursor.execute(sql, values)
    product_id = cursor.lastrowid
    conn.commit()
    return {'product_added': 'ok'}


def get_products(email):
    cursor = get_connection().cursor()

    if email:
        cursor.execute("SELECT * FROM products where email = '" + email + "'")
    else:
        cursor.execute("SELECT * FROM products")

    rows = cursor.fetchall()

    result = []
    for row in rows:
        product = {}
        product['product_id'] = row[0]
        product['category_name'] = row[1]
        product['product_name'] = row[3]
        product['description'] = row[4]
        product['price'] = row[5]
        product['available_quantity'] = row[6]
        product['image'] = row[7]
        result.append(product)
    return result

def update_product(body):
    conn = get_connection()
    cursor = conn.cursor()
    product_id = body['product_id']
    result = []
    for key in body.keys():
        if not key == 'product_id':
            sql = "Update products set " + key + " = '" + str(body[key]) + "' where product_id = " + str(product_id)
            rows = cursor.execute(sql)
            response = {key: str(body[key])}
            result.append(response)
    product_id = cursor.lastrowid

    conn.commit()
    return {"Fields_Updated": result}

def get_orders(email):

    cursor = get_connection().cursor()

    cursor.execute("SELECT * FROM orders join order_details on order_details.order_id = orders.order_id join products p on order_details.product_id = p.product_id where p.email = '" + email + "'")

    rows = cursor.fetchall()

    processed_orders =[]
    result = []
    for row in rows:
        order_id = row[0]
        if order_id not in processed_orders:
            order = {'order_id': order_id}
            order['total_amount'] = row[1]
            order['created_on'] = str(row[2])
            order['status'] = row[3]
            order['products'] = []
            result.append(order)
            processed_orders.append(order_id)

    for row in rows:
        order_id = row[0]
        product = {}
        product['product_name'] = row[8]
        product['product_id'] = row[6]
        product['quantity'] = row[9]
        product['unit_cost'] = row[10]

        for i in range(len(result)):
            if result[i]['order_id'] == order_id:
                result[i]['products'].append(product)
    return result


def get_user(email):
    cursor = get_connection().cursor()
    cursor.execute("SELECT role FROM users where email = '"+email+"'")
    rows = cursor.fetchall()

    if len(rows) < 1:
        return None
    else:
        return {'role': rows[0][0]}

def add_or_update_user(body):

    current_role = get_user(body['email'])

    if current_role:
        current_role = current_role['role']
    conn= get_connection()
    cursor = conn.cursor()

    if not current_role:
        sql = "Insert into users (first_name, last_name, email, token, role)  values (%s, %s,%s, %s,%s)"
        values = (body['first_name'], body['last_name'],  body['email'], body['token'], 'Seller')
        rows = cursor.execute(sql, values)
    elif current_role == 'Seller':
        sql = "Update users SET role = 'Buyer-Seller' , token = '" + body['token'] +"' where email = '" +body['email']+ "'"
        rows = cursor.execute(sql)
    elif current_role == 'Buyer' or current_role == 'Buyer-Seller':
        sql = "Update users SET token = '" + body['token'] +"' where email = '" +body['email']+ "'"
        rows = cursor.execute(sql)

    conn.commit()

    return True