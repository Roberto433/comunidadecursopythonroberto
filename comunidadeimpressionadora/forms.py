from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField("Nome de Usuáiro", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha =PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação da Senha", validators=[DataRequired(), EqualTo('senha') ])
    botao_submit_criarconta = SubmitField("Criar Conta")

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField("Fazer Login")

class FormEditarPerfil(FlaskForm):
    username = StringField("Nome de Usuáiro", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

    curso_excel = BooleanField('Excel Impressionador')
    curso_vba= BooleanField('VBA Impressionador')
    curso_powerbi = BooleanField('Power Bi Impressionador')
    curso_pauthon = BooleanField('Python Impressionador')
    curso_ppt = BooleanField('Apresentações Impressionadoras')
    curso_sql = BooleanField('SQL Impressionador')
    botao_submit_editarperfil = SubmitField("Comfirmar Edição")

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError("Já existe um usuário com este e-mail. Cadastre outro e-mail")

class FormCriarPost(FlaskForm):
    titulo = StringField("Titulo do Post", validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu Post Aqui', validators=[DataRequired()])
    botao_submit = SubmitField("Criar Post")