from flask_restful import reqparse

computer_parser = reqparse.RequestParser()
computer_parser.add_argument(
    "hard_drive_type", type=str, required=True, help="hard_drive_type cannot be empty"
)
computer_parser.add_argument(
    "processor", type=str, required=True, help="processor cannot be empty"
)
computer_parser.add_argument(
    "ram_amount", type=int, required=True, help="ram_amount cannot be empty"
)
computer_parser.add_argument(
    "maximum_ram", type=int, required=True, help="maximum_ram cannot be empty"
)
computer_parser.add_argument(
    "form_factor", type=str, required=True, help="form_factor cannot be empty"
)
