from flask import Flask, flash, redirect, request, url_for
import os
from markdown import markdown
from werkzeug.utils import secure_filename


def read(app: Flask, note_filename: str):
    with open(
        os.path.join(app.config["UPLOAD_FOLDER"], f"{note_filename}"), "r"
    ) as file:
        return file.read()


def read_html(app: Flask, note_filename: str):
    with open(
        os.path.join(app.config["UPLOAD_FOLDER"], f"{note_filename}"), "r"
    ) as file:
        note = file.read()
        return markdown(note)


def save_file(app: Flask, file):
    filename = secure_filename(file.filename)
    if not filename.endswith(".md"):
        flash("Only markdown files are allowed")
        return redirect(request.url)
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], f"{filename}"))
    flash("File uploaded successfully")
