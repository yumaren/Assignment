import os
import sys
from flask import Flask, render_template, request, redirect, send_file, url_for
from config.py import list_files, download_file, upload_file

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
bucket = "assignment-utp1-8775de9e-217c-4e3a-9660-3d91f90602b1"


# @app.route('/')
# def entry_point():
#      if request.method == 'POST':
#         bucket = request.form['bucket']
#         session['bucket'] = bucket
#         return redirect(url_for('files'))
#         # else
        # buckets = get_buckets_list()
        # return render_template("index.html", buckets=buckets)

@app.route('/')
def entry_point():
    # return 'Project completed by Yumaren & Jeevan'
    return render_template('index.html')

    
# @app.route("/create",  methods=['POST'])
# def create_bucket():
#  if request.method == "POST":
#         btext = request.form["u"]
# #         # f = request.files['file']
# #         # f.save(f.filename)
#         # f.save(f.filename)
#         create_bucket(f"{btext}")

#         return redirect("/")

@app.route("/storage")
def storage():
    contents = list_files("upload")
    return render_template('upload.html', contents=contents)


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(f.filename)
        upload_file(f"{f.filename}", bucket)

        return redirect("/storage")


@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, bucket)

        return send_file(output, as_attachment=True)


@app.route('/delete', methods=['POST'])
def delete():
    key = request.form['key']

    my_bucket = get_bucket()
    my_bucket.Object(key).delete()

    flash('File deleted successfully')
    return redirect(url_for('files'))


if __name__ == '__main__':
    app.run(debug=True)
