from flask import render_template, flash,request,redirect, url_for, current_app
from app import db
import os
from .models import Items
from .helper import get_vendor_name, save_photo

def view(name):
    datas = Items.query.filter(Items.name == name).all()
    
    print(datas)
        
    if not datas:
        flash("No data found",'danger')
    return render_template(
                        'vendor/vendor_view.html',
                        datas=datas
                        )
    
def upload():
    if request.method == 'POST':
        ERR_MSG = None
        name = request.form.get('vendor')
        d_no = request.form.get('d_no')
        rate = request.form.get('rate')
        final_stones = request.form.get('final_stones')
        img = save_photo(request.files.get('img'))
        
        if ERR_MSG is not None:
            flash(ERR_MSG,'danger')
        else:
            if not img:
                flash("Bad upload",'danger')
            data = Items(
                        name=name,
                        d_no = d_no,
                        rate=rate,
                        final_stones=final_stones,
                        img=img
                        )            
            db.session.add(data)
            db.session.commit()
            
            flash("Uploaded Successfully!!", "info")
            
            return redirect(url_for(
                                'views.view',
                                name = name
                                )
                            )
    name = get_vendor_name()
    
    return render_template(
                        'vendor/upload_form.html',
                        name=name
                        )
    
def update(id,name):
    
    data = Items.query.get_or_404(id,name)
    print(data)
    
    if request.method == 'POST':
        ERR_MSG = None
        data.name = request.form.get('vendor')
        data.d_no = request.form.get('d_no')
        data.rate = request.form.get('rate')
        data.final_stones = request.form.get('final_stones')
        
        if request.files.get('img'):
            os.unlink(os.path.join(current_app.root_path, 'static/img/' + data.img))
            data.img = save_photo(request.files.get('img'))           
        
        if ERR_MSG is not None:
            flash(ERR_MSG,'danger')
        else:
            # db.session.merge(data)
            db.session.commit()
            flash(f"{data.name.capitalize()} Updated Successfully!!", "info")
            return redirect(url_for(
                                'views.view',
                                name = data.name
                                )
                            )
            
    name = get_vendor_name()
    return render_template(
                        'vendor/update_vendor.html',
                        data=data,
                        name=name
                        )
    
def delete(id,name) :
    post = Items.query.get_or_404(id,name)
    print(post)
    
    os.unlink(os.path.join(current_app.root_path, 'static/img/' + post.img))
    
    db.session.delete(post)
    db.session.commit()
    
    flash(f'{post.name} Deleted successfully!!','danger')
    
    return redirect(url_for(
                        'views.view',
                        name = post.name
                        )
                    )