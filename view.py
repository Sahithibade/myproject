from flask import Blueprint, render_template, request
from pymysql import connections
import os

# Configure the database connection
db = connections.Connection(
    host="database-4.caus9udfh4nq.us-east-2.rds.amazonaws.com",
    user="admin",
    port= 3306,
    password="admin123",
    database="Giftstore"
    
    
)

imagepath = os.path.join('static', 'giftimage.jpg')
auth_bp = Blueprint('view', __name__)

@auth_bp.route('/')
def index():
    return render_template('login.html', image=imagepath)
   

@auth_bp.route('/loginpage')



def loginpage():
    return render_template('login.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    if result:
            return render_template('main.html', image=imagepath,image1=imagepath1,image2=imagepath2,image3=imagepath3,image4=imagepath4,image5=imagepath5,image6=imagepath6,image7=imagepath7,image8=imagepath8,image9=imagepath9,image10=imagepath10,image11=imagepath11,image12=imagepath12,image13=imagepath13,image14=imagepath14,image15=imagepath15,image16=imagepath16,image18=imagepath18,image17=imagepath17)

    else:
        return 'Login failed'
imagepath1 = os.path.join('static', 'anniversary1.jpg')
imagepath2= os.path.join('static', 'anniversary2.jpg')
imagepath3 = os.path.join('static', 'anniversary3.jpg')
imagepath4 = os.path.join('static', 'anniversary4.webp')
imagepath5 = os.path.join('static', 'birthday1.webp')
imagepath6 = os.path.join('static', 'birthday2.webp')
imagepath7 = os.path.join('static', 'birthday3.jpg')
imagepath8 = os.path.join('static', 'birthday4.jpg')
imagepath9 = os.path.join('static', 'giftcard1.jpg')
imagepath10 = os.path.join('static', 'giftcard2.png')
imagepath11 = os.path.join('static', 'giftcard3.jpg')
imagepath12 = os.path.join('static', 'giftcard4.webp')
imagepath13 = os.path.join('static', 'valentines1.gif')
imagepath14 = os.path.join('static', 'valentines2.jpg')
imagepath15 = os.path.join('static', 'valentines3.jpg')
imagepath16 = os.path.join('static', 'valentines4.jpg')
imagepath17 = os.path.join('static', 'logo.jpg')
imagepath18 = os.path.join('static', 'specialoffer.jpg')

@auth_bp.route('/registerpage')
def registerpage():
    imagepath = os.path.join('static', 'giftimage.jpg')
    return render_template('createaccount.html',image=imagepath)
@auth_bp.route('/register', methods=['POST'])
def register():
    cursor = db.cursor()
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if password != confirm_password:
        return 'Passwords do not match'
    else:
        # Execute the INSERT query to add a new user to the database
        cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        return render_template('main.html', image=imagepath,image1=imagepath1,image2=imagepath2,image3=imagepath3,image4=imagepath4,image5=imagepath5,image6=imagepath6,image7=imagepath7,image8=imagepath8,image9=imagepath9,image10=imagepath10,image11=imagepath11,image12=imagepath12,image13=imagepath13,image14=imagepath14,image15=imagepath15,image16=imagepath16,image18=imagepath18,image17=imagepath17)


@auth_bp.route('/main', methods=['POST'])
def main():
    cursor = db.cursor()
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if password != confirm_password:
        return 'Passwords do not match'
    else:
        # Execute the INSERT query to add a new user to the database
        cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        return render_template('main.html')
imagepath18 = os.path.join('static', 'giftkit1.jpeg')
imagepath19 = os.path.join('static', 'giftkit2.webp')
imagepath20 = os.path.join('static', 'giftkit3.webp')
imagepath21 = os.path.join('static', 'giftki4.webp')
imagepath17 = os.path.join('static', 'logo.jpg')
imagepath18 = os.path.join('static', 'specialoffer.jpg')

@auth_bp.route('/ordering')
def about():
    return render_template('contact.html', image=imagepath,image18=imagepath18,image19=imagepath19,image21=imagepath21,image17=imagepath17)

@auth_bp.route('/ordering', methods=['POST'])
def giftordering():
    cursor = db.cursor()
    giftname = request.form['giftname']
    number_of_gifts = request.form['gifts']
    name = request.form['name']
    email=request.form['email']
    comments=request.form['comments']
    address=request.form['address']
    # Execute the INSERT query to add a new user to the database
    cursor.execute("INSERT INTO giftstore (giftname,number_of_gifts,name,email,comments,address) VALUES (%s, %s,%s)", (giftname,number_of_gifts,name,email,comments,address))
    db.commit()
    return render_template('main.html')
