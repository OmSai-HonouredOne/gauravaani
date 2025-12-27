from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort

from gauravaani.auth import login_required
from gauravaani.db import query_all, query_one, query
from gauravaani import get_params


bp = Blueprint('courses', __name__)
params = get_params()

@bp.route('/')
def index():
    courses = query_all(
        'SELECT cid, course_id, course_title, course_description, course_image'
        ' FROM courses'
        ' ORDER BY cid DESC'
    )
    return render_template('courses/index.html', courses=courses, params=params)


@bp.route('/courses')
def courses():
    courses = query_all(
        'SELECT cid, course_id, course_title, course_description, course_image'
        ' FROM courses'
        ' ORDER BY cid ASC'
    )
    return render_template('courses/courses.html', courses=courses, params=params)


@bp.route('/courses/<string:course_id>/view')
def view_course(course_id):
    course = query_one('SELECT * FROM courses WHERE course_id = %s', (course_id,))
    lectures = query_all(
        'SELECT * FROM lectures WHERE cid = %s ORDER BY course_chapter ASC, lec_no ASC', (course['cid'],)
    )
    if course is None:
        abort(404, f"Course id {course_id} doesn't exist.")
    return render_template('courses/view_course.html', course=course, lectures=lectures, params=params)


@bp.route('/courses/<string:course_id>/view/<int:course_chapter>/<int:lec_no>')
def view_lecture(course_id, course_chapter, lec_no):
    course = query_one('SELECT * FROM courses WHERE course_id = %s', (course_id,))
    lecture = query_one(
        'SELECT * FROM lectures WHERE cid = %s AND course_chapter = %s AND lec_no = %s',
        (course['cid'], course_chapter, lec_no)
    )
    all_lectures = query_all(
        'SELECT * FROM lectures WHERE cid = %s ORDER BY course_chapter ASC, lec_no ASC', (course['cid'],)
    )
    if course is None:
        abort(404, f"Course id {course_id} doesn't exist.")
    if lecture is None:
        abort(404, f"Lecture number {lec_no} in chapter {course_chapter} doesn't exist for course id {course_id}.")
    return render_template('courses/view_lecture.html', course=course, lecture=lecture, all_lectures=all_lectures, params=params)