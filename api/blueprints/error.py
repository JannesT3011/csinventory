from flask import Blueprint, redirect, url_for, render_template

error = Blueprint("error", __name__, url_prefix="/error")

@error.app_errorhandler(404)
def hanlde_404_error(e):
    return "Not found!", 404

@error.app_errorhandler(405)
def hanlde_405_error(e):
    return redirect("/"), 200