from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Entry
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    cpf = request.form['cpf']
    phone = request.form['phone']
    action = request.form['action']

    if action == 'Saída':
        last_entry = Entry.query.filter_by(name=name, action='Entrada').order_by(Entry.timestamp.desc()).first()

        if last_entry:
            cpf = last_entry.cpf
            phone = last_entry.phone
        else:
            flash('Erro: Nenhum registro de entrada encontrado para esse nome.', 'error')
            return redirect(url_for('main.index'))
    else:
        if not cpf or not phone:
            flash('Erro: CPF e telefone são obrigatórios para registrar uma entrada.', 'error')
            return redirect(url_for('main.index'))

    new_entry = Entry(name=name, cpf=cpf, phone=phone, action=action)
    db.session.add(new_entry)
    db.session.commit()

    flash('Registro efetuado com sucesso!', 'success')
    return redirect(url_for('main.index'))

@main.route('/delete_entry/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    try:
        db.session.delete(entry)
        db.session.commit()
        flash('Registro apagado com sucesso!')
    except Exception as e:
        db.session.rollback()
        flash('Erro ao tentar apagar o registro.', 'error')
    return redirect(url_for('main.records'))

@main.route('/records', methods=['GET'])
def records():
    entries = Entry.query.all()
    return render_template('records.html', entries=entries)