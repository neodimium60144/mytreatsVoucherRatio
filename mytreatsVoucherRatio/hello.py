from flask import Flask,render_template, request ,redirect, url_for,flash
from flask_mysqldb import MySQL

from flask_cors import CORS

from flask import jsonify

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/unema/imageflask'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['SECRET_KEY'] = 'baim'
app.config['MYSQL_HOST'] = 'exadev.mytreats.asia'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'devserver'
app.config['MYSQL_DB'] = 'mytreats'

CORS(app)

mysql = MySQL(app)

@app.route('/mytreats_voucher_ratio')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM mytreats_voucher_ratio''')
    rv = cur.fetchall()
 #  return str(rv)

    rv ={
    "ratio_mytreats": "1",
    "ratio_addon": "1",
    "monthyear": "2019-04",
    "status": "0",

    "ratio_mytreats": "1",
    "ratio_addon": "1",
    "monthyear": "2019-05",
    "status": "0",
    }

    return jsonify(rv)


@app.route('/create', methods=["POST"])
def create():
    ratio_mytreats = request.form['ratio_mytreats']
    ratio_addon = request.form['ratio_addon']
    monthyear = request.form['monthyear']
    status = request.form['status']

#   return price
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO mytreats_voucher_ratio (ratio_mytreats, ratio_addon, monthyear, status) VALUES (%s,%s,%s,%s)", (ratio_mytreats,ratio_addon,monthyear,status))
    mysql.connection.commit()
    return "sukses"

@app.route('/update', methods=["POST"])
def update():
    ratio_mytreats = request.form['ratio_mytreats']
    ratio_addon = request.form['ratio_addon']
    monthyear = request.form['monthyear']
    status = request.form['status']

    cur = mysql.connection.cursor()
    # cur.execute("UPDATE promotion_save (partner_id,title,price,discount_price,image,qty,start_date,end_date,qr_code,status,description,created_at,updated_at) VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (title,harga,discount_price,image,qty,start_date,end_date,qr_code,status,description,created_at,updated_at))
    #"UPDATE promotion save SET title=baim,image=dsadsa,price=333 where id = 1 "
    cur.execute("UPDATE promotion_save SET title=title,image=image,price=500 where id =1")
    mysql.connection.commit()
    return "sukses"

@app.route('/hapus/<string:id_data>', methods=["GET"])
def hapus(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM promotion_save WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return "sukses"

'''
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
'''
'''
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
'''
'''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
'''
'''
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']

      f.save(secure_filename(f.filename))
      return render_template('end.html')
'''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_gambar', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        # This will be executed on POST request.
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # flash("File uploaded: Thanks!", "success")
            return "sukses"


if __name__ == '__main__':
    app.run(debug=True)