
from flask import Flask,request,render_template,url_for,redirect
from mydatabase import MyDatabase
app=Flask(__name__)




@app.route('/',methods=['GET','POST'])
def viewform():
    if request.method=='GET':
        return render_template("form.html")
    elif request.method=='POST':
        tit=request.form['tit']
        desc=request.form['desc']
        date=request.form['date']
        print(tit,desc,date)
        mydb=MyDatabase()
        sql=f"insert into company(tit,desc,date)values('{tit}','{desc}','{date}')"
        mydb.insert(sql)
        return render_template('form.html',msg="post method worked")


@app.route('/vw',methods=['GET','POST'])
def view():
    mydb=MyDatabase()
    data=mydb.view()
    print(data)
    return render_template('formview.html',data=data)

@app.route('/edit/<id>',methods=['GET','POST'])
def edit(id):
    print(id)
    if request.method=='GET':
        mydb=MyDatabase()
        sql="select * from company where id='"+id+"'"
        data=mydb.selectone(sql)
        print(data)
        return render_template("edit.html",data=data)
    else:
        tit=request.form['tit']
        desc=request.form['desc']
        date=request.form['date']
        print(tit,desc,date)
        mydb=MyDatabase()
        sql='update company set tit="'+tit+'",desc="'+desc+'",date="'+date+'"where id="'+id+'"'
        mydb.update(sql)
        return redirect(url_for('view'))


@app.route('/del/<id>',methods=['GET','POST'])
def delete(id):
    print(id)
    mydb=MyDatabase()
    sql='DELETE FROM company WHERE id="'+id+'"'
    mydb.delete(sql)
    return redirect(url_for('view'))

if __name__=='__main__':
    app.run(debug=True)
