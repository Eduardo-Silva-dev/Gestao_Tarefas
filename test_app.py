import unittest
from app import app, db, Task
from flask_testing import TestCase

class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True

class TaskManagerTestCase(TestCase):
    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        db.create_all()
        # Adiciona uma tarefa inicial para os testes
        task = Task(title='Test Task', description='This is a test task.')
        db.session.add(task)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_task(self):
        response = self.client.post('/tasks', json={
            'title': 'New Task',
            'description': 'This is a new task'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Tarefa criada com sucesso', response.data)

    def test_get_tasks(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Task', response.data)

    def test_update_task(self):
        task = Task.query.first()
        response = self.client.patch(f'/tasks/{task.id}', json={
            'title': 'Updated Task Title'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tarefa atualizada com sucesso', response.data)
        task = Task.query.get(task.id)
        self.assertEqual(task.title, 'Updated Task Title')

    def test_delete_task(self):
        task = Task.query.first()
        response = self.client.delete(f'/tasks/{task.id}')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(Task.query.get(task.id))

    def test_complete_task(self):
        task = Task.query.first()
        response = self.client.put(f'/tasks/{task.id}/complete')
        self.assertEqual(response.status_code, 200)
        task = Task.query.get(task.id)
        self.assertTrue(task.completed)
        self.assertIsNotNone(task.completed_at)

if __name__ == '__main__':
    unittest.main()
