from flask import Blueprint
from .helper import *
from .customer import *
from .vendors import *


views = Blueprint('views', __name__)

@views.route('/')
def home():
        
    return render_template(
                        'home.html'
                        )

views.add_url_rule('/create-customer',view_func=create_customer,methods=['GET','POST'])

views.add_url_rule('/update/<int:id>/customer', view_func=update_customer,methods = ['GET','POST'])

views.add_url_rule('/delete/<int:id>/customer',view_func=delete_customer)

views.add_url_rule('/customer-details',view_func=customer_details)        

views.add_url_rule('/view/<name>',view_func=view)

views.add_url_rule('/upload',view_func=upload , methods=['GET','POST'])

views.add_url_rule('<name>/<int:id>/update',view_func=update, methods = ['GET','POST'])

views.add_url_rule('<name>/<int:id>/delete',view_func=delete)

views.add_url_rule('/customer-entry',view_func=book_entry ,methods=['GET','POST'])

views.add_url_rule('/customer-view/<int:id>',view_func=cust_entry_view)

views.add_url_rule('/delete/<int:id>',view_func=delete_entry)