import unittest
from unittest.mock import patch, Mock
from api import app


class TestComputerApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch("models.Computer.query")
    def test_get_all_computers(self, mock_query):
        mock_computer = Mock()
        mock_computer.id = 1
        mock_computer.hard_drive_type = "ssd"
        mock_computer.processor = "Intel i7"
        mock_computer.ram_amount = 16
        mock_computer.maximum_ram = 32
        mock_computer.form_factor = "Laptop"
        mock_query.all.return_value = [mock_computer]

        response = self.app.get("/api/computers/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"hard_drive_type": "ssd"', response.data)

    @patch("api.db.session")
    @patch("models.Computer.query")
    def test_post_computer(self, mock_query, mock_session):
        mock_session.add = Mock()
        mock_session.commit = Mock()

        mock_computer = Mock()
        mock_computer.id = 1
        mock_computer.hard_drive_type = "ssd"
        mock_computer.processor = "Intel i7"
        mock_computer.ram_amount = 16
        mock_computer.maximum_ram = 32
        mock_computer.form_factor = "Laptop"
        mock_query.all.return_value = [mock_computer]

        response = self.app.post(
            "/api/computers/",
            json={
                "hard_drive_type": "ssd",
                "processor": "Intel i7",
                "ram_amount": 16,
                "maximum_ram": 32,
                "form_factor": "Laptop",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'"hard_drive_type": "ssd"', response.data)

    @patch("models.Computer.query")
    def test_get_single_computer(self, mock_query):
        mock_computer = Mock()
        mock_computer.id = 1
        mock_computer.hard_drive_type = "hdd"
        mock_computer.processor = "Intel i5"
        mock_computer.ram_amount = 8
        mock_computer.maximum_ram = 16
        mock_computer.form_factor = "Desktop"
        mock_query.get.return_value = mock_computer

        response = self.app.get("/api/computers/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"processor": "Intel i5"', response.data)

    @patch("api.db.session")
    @patch("models.Computer.query")
    def test_patch_single_computer(self, mock_query, mock_session):
        mock_computer = Mock()
        mock_computer.id = 1
        mock_computer.hard_drive_type = "SSD"
        mock_computer.processor = "Intel i7"
        mock_computer.ram_amount = 16
        mock_computer.maximum_ram = 32
        mock_computer.form_factor = "Desktop"

        mock_query.filter_by.return_value.first.return_value = mock_computer
        mock_session.commit = Mock()

        response = self.app.patch(
            "/api/computers/1",
            json={
                "hard_drive_type": "hdd",
                "processor": "Intel i5",
                "ram_amount": 4,
                "maximum_ram": 8,
                "form_factor": "Laptop",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"hard_drive_type": "hdd"', response.data)

    @patch("api.db.session")
    @patch("models.Computer.query")
    def test_delete_single_computer(self, mock_query, mock_session):
        mock_computer = Mock()
        mock_computer.id = 1
        mock_computer.hard_drive_type = "hdd"
        mock_computer.processor = "Intel i5"
        mock_computer.ram_amount = 8
        mock_computer.maximum_ram = 16
        mock_computer.form_factor = "Desktop"

        mock_query.get.return_value = mock_computer
        mock_query.all.return_value = []
        mock_session.delete = Mock()
        mock_session.commit = Mock()

        response = self.app.delete("/api/computers/1")
        self.assertEqual(response.status_code, 200)
        mock_session.delete.assert_called_once_with(mock_computer)
        self.assertIn(b"[]", response.data)
