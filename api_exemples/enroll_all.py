"""
Example to enroll a user in all courses using the REST API.
"""

import requests

username = 'papa'
password = 'room.test'

base_url = 'http://127.0.0.1:8000/api/'

# retrieve all courses
r = requests.get('{}courses/'.format(base_url))
courses = r.json()

available_courses = ', '.join([course['title'] for course in courses])
print('Available courses: {}'.format(available_courses))

for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post('{}courses/{}/enroll/'.format(base_url, course_id), auth=(username, password))

    if r.status_code == 200:
        # successfull request
        print(f'successfully enrolled in: {course_title}')