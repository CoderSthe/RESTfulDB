from flask_restful import Resource, marshal_with, abort

from db_setup import db
from models import Computer
from parsers import computer_parser
from schemas import computer


class Computers(Resource):
    @marshal_with(computer)
    def get(self):
        computers = Computer.query.all()
        return computers

    @marshal_with(computer)
    def post(self):
        args = computer_parser.parse_args()
        computer = Computer(
            hard_drive_type=args["hard_drive_type"],
            processor=args["processor"],
            ram_amount=args["ram_amount"],
            maximum_ram=args["maximum_ram"],
            form_factor=args["form_factor"],
        )
        db.session.add(computer)
        db.session.commit()
        return Computer.query.all(), 201


class SingleComputer(Resource):
    @marshal_with(computer)
    def get(self, id):
        computer = Computer.query.get(id)
        if not computer:
            abort(404, description="Computer not found.")
        return computer

    @marshal_with(computer)
    def patch(self, id):
        args = computer_parser.parse_args()
        computer = Computer.query.get(id)
        if not computer:
            abort(404, description="Computer not found.")

        for field, value in args.items():
            if value is not None:
                setattr(computer, field, value)

        db.session.commit()
        return computer

    @marshal_with(computer)
    def delete(self, id):
        computer = Computer.query.get(id)
        if not computer:
            abort(404, description="Computer not found.")
        db.session.delete(computer)
        db.session.commit()
        return Computer.query.all()
