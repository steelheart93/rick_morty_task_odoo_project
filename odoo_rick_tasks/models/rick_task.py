from odoo import models, fields

class RickTask(models.Model):
    _name = 'rick.task'
    _description = 'Tarea externa con personaje de Rick and Morty'

    title = fields.Char(string='Título', required=True)
    description = fields.Text(string='Descripción')
    due_date = fields.Date(string='Fecha límite')
    status = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada'),
    ], default='pendiente', string='Estado')

    character_name = fields.Char(string='Personaje')
    character_image = fields.Char(string='Imagen')
