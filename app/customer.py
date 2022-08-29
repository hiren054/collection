from flask import render_template,redirect,url_for,request,flash
from .models import Users,Book
from app import db
from .helper import get_customer_details

def create_customer():
    if request.method == 'POST':
        print("\n\n\n\nINSIDE CREATE_CUSTOMER\n\n\n\n")
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        
        user = Users(
                    name=name,
                    phone_number=phone_number
                    )
        
        db.session.add(user)
        db.session.commit()
        
        flash('Customer created Successfully!!','info')
        
        return redirect(url_for(
                            'views.customer_details'
                            )
                        )

    return render_template('customer/create_customer.html')

def update_customer(id):
    user = Users.query.get_or_404(id)
    
    print(user)
    
    if request.method == 'POST':
        print("\n\n\n\nINSIDE CREATE_CUSTOMER\n\n\n\n")
        user.name = request.form.get('name')
        user.phone_number = request.form.get('phone_number')
        
        db.session.commit()
        
        flash(f'Customer {user.name} Update Successfully!!','info')
        
        return redirect(url_for('views.customer_details'))

    return render_template('customer/update_customer.html',user=user)

def delete_customer(id):
    user = Users.query.get_or_404(id)
    print(user)
    
    db.session.delete(user)
    db.session.commit()
    
    flash(f'Customer {user.name} Deleted','danger')
    
    return redirect(url_for('views.customer_details'))

def customer_details():
    
    users = get_customer_details()
    
    print(users)
      
    return render_template(
                            'customer/customer_details.html',
                            users=users
                            )
    
def book_entry():
    names = get_customer_details()
    print(names)
    
    if request.method == 'POST':
        print('\n\n\n\nINSIDE ENTRY_BOOK\n\n\n\n')
        qty = request.form.get('qty')
        detail = request.form.get('detail')
        rate = request.form.get('rate')
        total = request.form.get('total')
        customer_id = request.form.get('customer_id')
        print(qty,rate,total,customer_id)

        book = Book(qty=qty,
                    detail=detail,
                    rate=rate,
                    total=total,
                    customer_id=customer_id)

        db.session.add(book)
        db.session.commit()

        flash('Record submitted successfully','info')
        
        return redirect(url_for('views.customer_details'))

    return render_template('book/entry.html',names=names)

def cust_entry_view(id):
    books = Book.query.filter(Book.customer_id==id).all()
    
    gr_total = [int(i.total) for i in books]
    
    print(len(books))
    if len(books) != 0:
        name = books[0].users.name
        # flash('No any records!! Create new record','warning')
        return render_template('book/cust_entry_view.html',books=books,name=name,gr_total=sum(gr_total))
    return(redirect(url_for('views.book_entry')))

def delete_entry(id):
    book = Book.query.get_or_404(id)
    print(book)
    db.session.delete(book)
    db.session.commit()

    print('\n\n\n\nBook Deleted\n\n\n\n')
    return redirect(url_for('views.cust_entry_view',id=book.id))