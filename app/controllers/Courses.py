"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Course')
        self.db = self._app.db

        """

        This is an example of a controller method that will load a view for the client

        """

    def index(self):
        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_users()

        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """
        all_course = self.models['Course'].get_all_courses()
        return self.load_view('index.html', courseinfo = all_course)

    def add(self):
        course_details = {
            'name': request.form['name'],
            'description': request.form['description']
        }
        self.models['Course'].add_course(course_details)
        return redirect('/')

    def destroy(self, id):
        one_course = self.models['Course'].get_course_by_id(id)
        print one_course
        return self.load_view('confirm.html', one_course = one_course)

    def delete(self, id):
        self.models['Course'].delete(id)
        return redirect('/')
