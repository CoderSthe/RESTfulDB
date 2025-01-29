from flask_restful import fields

computer = {
    "id": fields.Integer,
    "hard_drive_type": fields.String,
    "processor": fields.String,
    "ram_amount": fields.Integer,
    "maximum_ram": fields.Integer,
    "form_factor": fields.String,
}
