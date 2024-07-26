from flask import Blueprint, render_template, request, jsonify
from models.employeeModel import db, Employee

employee_blueprint = Blueprint('employee_blueprint', __name__)

@employee_blueprint.route('/')
def main_page():
    return render_template('mainpage.html')

@employee_blueprint.route('/create')
def create_page():
    return render_template('createpage.html')

@employee_blueprint.route('/employees', methods=['POST'])
def create_employee():
    # Verifica se o Content-Type da requisição é 'application/json'
    if request.content_type != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 415  # Unsupported Media Type

    # Tenta obter os dados JSON da requisição
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON data received'}), 400  # Bad Request

    # Cria um novo funcionário com os dados recebidos
    new_employee = Employee(name=data['name'], position=data['position'], salary=data['salary'])
    db.session.add(new_employee)
    db.session.commit()

    # Retorna o novo funcionário criado como resposta JSON
    return jsonify(new_employee.to_dict()), 201

@employee_blueprint.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.to_dict() for employee in employees])

@employee_blueprint.route('/employees/list')
def employees_page():
    return render_template('employees.html')