from app.models import Employee, db

class EmployeeService:
    @staticmethod
    def get_all_employees():
        return [{'id': e.id, 'name': e.name, 'position': e.position} 
                for e in Employee.query.all()]

    @staticmethod
    def get_employee_by_id(id):
        employee = Employee.query.get_or_404(id)
        return {'id': employee.id, 'name': employee.name, 'position': employee.position}
