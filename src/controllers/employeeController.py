from flask import Blueprint, render_template

employee_blueprint = Blueprint('employee', __name__)

@employee_blueprint.route('/')
def index():
    return render_template('mainpage.html')