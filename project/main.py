from io import BytesIO

from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from PIL import Image

from . import receipts
from .models import Receipt
from .processing import detect_text


main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST" and "photo" in request.files:
        filename = receipts.save(request.files["photo"])
        rec = Receipt(filename=filename)
        rec.store()
        flash("Photo saved.")
        return redirect(url_for("main.show", receipt_id=rec.id))
    return render_template("upload.html", name=current_user.name)


@main.route("/receipt/<receipt_id>")
def show(receipt_id):
    receipt = Receipt.load(receipt_id)
    if receipt is None:
        abort(404)
    url = receipts.url(receipt.filename)
    path = "/tmp/receipts/" + receipt.filename
    texts = detect_text(path)

    return render_template("show.html", url=url, texts=texts)
