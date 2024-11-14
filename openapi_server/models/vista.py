from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def import_db(database):
    global db
    db = database
    
class Vistas(db.Model):
    tablename = 'vistas'
    
    id_vista = db.Column(db.Integer, primary_key=True)
    nombre_vista = db.Column(db.String(255), nullable=False)
    contenidos_ids = db.Column(db.ARRAY(db.Integer)) 

    def repr(self):
        return f"<Vista(id_vista={self.id_vista}, nombre_vista='{self.nombre_vista}', contenidos_ids={self.contenidos_ids})>"
    
    def to_dict(self):
        return {
            "id_vista": self.id_vista,
            "nombre_vista": self.nombre_vista,
            "contenidos": self.contenidos_ids
        }
