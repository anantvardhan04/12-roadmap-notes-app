from flask import Flask, render_template, request, redirect, url_for, flash
import os
from markdown import markdown
from utils.file_ops import read, read_html, save_file
from form import NoteForm
from utils.language_tool import tool


# define routes
def register_routes(app: Flask):
    @app.route("/notes")
    def home():
        notes_list = os.listdir(app.config["UPLOAD_FOLDER"])
        return render_template("index.html", notes=notes_list)

    @app.route("/upload", methods=["GET", "POST"])
    def upload():
        form = NoteForm()
        if request.method == "POST" and form.validate_on_submit():
            save_file(app, form.file.data)
            return redirect(url_for("home"))
        return render_template("upload.html", form=form)

    @app.route("/note/<note_filename>")
    def notes(note_filename=None):
        note_content = read_html(app, note_filename)
        return render_template("note.html", note_content=note_content)

    @app.route("/check_grammar", methods=["POST"])
    def check_grammar():
        # initalise the language tool
        note_full_path = request.args.get("note_path")
        note_filename = os.path.basename(note_full_path)
        note_content = read(app, note_filename)
        issues = tool.check(note_content)
        return render_template("check_grammar.html", issues=issues)
