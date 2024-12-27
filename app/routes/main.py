from flask import Blueprint, render_template

# Define the blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/ibm')
def ibm():
    return render_template('ibm.html')

@main_bp.route('/nutanix')
def nutanix():
    return render_template('nutanix.html')

@main_bp.route('/vmware')
def vmware():
    return render_template('vmware.html')

@main_bp.route('/department')
def department():
    return render_template('core_banking_and_enterprise_system.html')

@main_bp.route('/price')
def price_calculator():
    return render_template('price_calculator.html')
