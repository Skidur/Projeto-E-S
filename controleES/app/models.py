from datetime import datetime, timezone, timedelta
from . import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    action = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def local_timestamp(self):
        # Define o fuso horário local
        local_tz = timezone(timedelta(hours=-3))  # UTC-3 para Brasília
        local_time = self.timestamp.replace(tzinfo=timezone.utc).astimezone(local_tz)
        return local_time.strftime('%d/%m/%Y %H:%M')  # Formata a data como D/M/A