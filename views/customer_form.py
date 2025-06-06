from PySide6.QtWidgets import QDialog, QMainWindow, QMessageBox
from ui.ui_customer_form import Ui_customer_form
from controllers.customer_controller import CustomerController

class CustomerForm(QDialog):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.ui = Ui_customer_form()
        self.ui.setupUi(self)

        parent_center_point = parent.geometry().center()
        self_geometry = self.frameGeometry()
        self_geometry.moveCenter(parent_center_point)
        self.move(self_geometry.topLeft())

        self.customer_controller = CustomerController()

        self.ui.save_btn.clicked.connect(self.save_customer)
    
    def save_customer(self):
        name = self.ui.name_input.text()
        email = self.ui.email_input.text()
        phone = self.ui.phone_input.text()

        if not name or not email or not phone:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
            return
        
        success = self.customer_controller.add({'name': name, 'email': email, 'phone': phone})

        if success:
            QMessageBox.information(self, "Sucesso", "Cliente cadastrado com sucesso.")
            self.accept()
        else:
            QMessageBox.critical(self, "Erro", "Erro ao salvar no banco de dados.")

        print(f"Salvando cliente: {name}, {email}, {phone}")