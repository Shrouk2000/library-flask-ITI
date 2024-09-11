import os
from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
from .model import Book
from .forms import BookForm
from . import db

book_blueprint = Blueprint('main', __name__)
UPLOAD_FOLDER = 'static/uploads'

def save_file(file):
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        return filename
    return None

@book_blueprint.route('/')
def index():
    books = Book.query.all()
    return render_template('book_list.html', books=books)

@book_blueprint.route('/book/<int:id>', methods=['GET', 'POST'])
def book_detail(id):
    book = Book.query.get_or_404(id)
    form = BookForm(obj=book)

    if request.method == 'POST':
        if form.validate_on_submit():
            if form.cover_photo.data:
                filename = save_file(form.cover_photo.data)
                if filename:
                    book.cover_photo = filename

            book.title = form.title.data
            book.number_of_pages = form.number_of_pages.data
            book.description = form.description.data

            db.session.commit()
            return redirect(url_for('main.book_detail', id=book.id))

    return render_template('book_detail.html', book=book, form=form)

@book_blueprint.route('/book/create', methods=['GET', 'POST'])
def create_book():
    form = BookForm()

    if form.validate_on_submit():
        filename = None
        if form.cover_photo.data:
            filename = save_file(form.cover_photo.data)

        new_book = Book(
            title=form.title.data,
            cover_photo=filename,
            number_of_pages=form.number_of_pages.data,
            description=form.description.data
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('create_book.html', form=form)

@book_blueprint.route('/book/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    form = BookForm(obj=book)

    if form.validate_on_submit():
        if form.cover_photo.data:
            filename = save_file(form.cover_photo.data)
            if filename:
                book.cover_photo = filename

        book.title = form.title.data
        book.number_of_pages = form.number_of_pages.data
        book.description = form.description.data

        db.session.commit()
        return redirect(url_for('main.book_detail', id=book.id))

    return render_template('edit_book.html', form=form, book=book)

@book_blueprint.route('/book/delete/<int:id>', methods=['POST'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('main.index'))
