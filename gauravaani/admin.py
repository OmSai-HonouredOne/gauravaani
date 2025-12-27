import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

import os

from gauravaani.db import query, query_one, query_all
from gauravaani.auth import admin_required
from gauravaani import get_params
from gauravaani.supabase_client import upload_course_image, delete_course_image


bp = Blueprint('admin', __name__, url_prefix='/admin')
params = get_params()



@bp.route('/')
@admin_required
def dashboard():
    return redirect(url_for('admin.manage_courses')) 
    # return render_template('admin/dashboard.html')



# User management routes
@bp.route('/users')
@admin_required
def manage_users():
    users = query_all('SELECT id, username, email, admin FROM users')
    return render_template('admin/users/manage_users.html', users=users, params=params)


@bp.route('/promote/<int:user_id>')
@admin_required
def promote_user(user_id):
    query('UPDATE users SET admin = TRUE WHERE id = %s', (user_id,))
    flash('User promoted to admin.')
    return redirect(url_for('admin.manage_users'))


@bp.route('/demote/<int:user_id>')
@admin_required
def demote_user(user_id):
    query('UPDATE users SET admin = FALSE WHERE id = %s', (user_id,))
    flash('User demoted from admin.')
    return redirect(url_for('admin.manage_users'))


@bp.route('/delete/<int:user_id>')
@admin_required
def delete_user(user_id):
    query('DELETE FROM users WHERE id = %s', (user_id,))
    flash('User deleted.')
    return redirect(url_for('admin.manage_users'))



# Course management routes
@bp.route('/courses')
@admin_required
def manage_courses():
    courses = query_all('SELECT cid, course_id, course_title, course_description, course_complete FROM courses ORDER BY cid ASC')
    return render_template('admin/courses/manage_courses.html', courses=courses, params=params)


@bp.route('/delete_course/<int:cid>')
@admin_required
def delete_course(cid):
    # Get course image URL before deleting record
    course = query_one(
        'SELECT course_image FROM courses WHERE cid = %s',
        (cid,)
    )

    # ✅ Delete image from Supabase if it exists
    if course and course['course_image']:
        delete_course_image(course['course_image'])

    # ✅ Delete course + related lectures
    query('DELETE FROM courses WHERE cid = %s', (cid,))
    query('DELETE FROM lectures WHERE cid = %s', (cid,))

    flash('Course deleted.')
    return redirect(url_for('admin.manage_courses'))


@bp.route('/add_course', methods=('GET', 'POST'))
@admin_required
def add_course():
    if request.method == 'POST':
        course_id = request.form['course_id']
        course_title = request.form['course_title']
        course_description = request.form['course_description']
        course_image = request.files['course_image']

        image_url = upload_course_image(course_image)

        query(
            'INSERT INTO courses (course_id, course_title, course_description, course_image) VALUES (%s, %s, %s, %s)',
            (course_id, course_title, course_description, image_url)
        )
        flash('Course added successfully.')
        return redirect(url_for('admin.manage_courses'))

    return render_template('admin/courses/add_course.html', params=params)


@bp.route('/edit_course/<int:cid>', methods=('GET', 'POST'))
@admin_required
def edit_course(cid):
    course = query_one('SELECT cid, course_id, course_title, course_description, course_image FROM courses WHERE cid = %s', (cid,))
    if request.method == 'POST':
        course_id = request.form['course_id']
        course_title = request.form['course_title']
        course_description = request.form['course_description']
        course_image = request.files['course_image']

        if course_image:
            delete_course_image(course['course_image'])
            new_course_image = upload_course_image(course_image)
        else:
            new_course_image = course['course_image']

        query(
            'UPDATE courses SET course_id = %s, course_title = %s, course_description = %s, course_image = %s WHERE cid = %s',
            (course_id, course_title, course_description, new_course_image, cid)
        )
        flash('Course updated successfully.')
        return redirect(url_for('admin.manage_courses'))

    return render_template('admin/courses/edit_course.html', course=course, params=params)


@bp.route('/toggle_course_status/<int:cid>')
@admin_required
def toggle_course_status(cid):
    row = query_one('SELECT course_complete FROM courses WHERE cid = %s', (cid,))
    current_status = row['course_complete']
    new_status = False if current_status else True
    query('UPDATE courses SET course_complete = %s WHERE cid = %s', (new_status, cid))
    flash('Course status updated.')
    return redirect(url_for('admin.manage_courses'))



# Lecture management routes
@bp.route('/courses/<string:course_id>')
@admin_required
def manage_lectures(course_id):
    course = query_one('SELECT course_id, course_title, course_description, course_image FROM courses WHERE course_id = %s', (course_id,))
    lectures = query_all(
        'SELECT lid, cid, course_chapter, lec_no, lec_title, lec_summary, lec_url, notes_url FROM lectures WHERE cid = (SELECT cid FROM courses WHERE course_id = %s) ORDER BY course_chapter ASC, lec_no ASC',
        (course_id,)
    )
    return render_template('admin/lectures/manage_lectures.html', lectures=lectures, course_id=course_id, course=course, params=params)

@bp.route('/courses/<string:course_id>/add_lecture', methods=('GET', 'POST'))
@admin_required
def add_lecture(course_id):
    course = query_one('SELECT * FROM courses WHERE course_id = %s', (course_id,))

    if request.method == 'POST':
        course_chapter = request.form['course_chapter']
        lec_no = request.form['lec_no']
        lec_title = request.form['lec_title']
        lec_summary = request.form['lec_summary']
        lec_url = request.form['lec_url']
        notes_url = request.form['notes_url']

        query(
            'INSERT INTO lectures (cid, course_chapter, lec_no, lec_title, lec_summary, lec_url, notes_url) VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (course['cid'], course_chapter, lec_no, lec_title, lec_summary, lec_url, notes_url)
        )
        flash('Lecture added successfully.')
        return redirect(url_for('admin.manage_lectures', course_id=course_id))

    return render_template('admin/lectures/add_lecture.html', course_id=course_id, course=course, params=params)

@bp.route('/courses/<string:course_id>/edit_lecture/<int:ch>/<int:lec_no>', methods=('GET', 'POST'))
@admin_required
def edit_lecture(course_id, ch, lec_no):
    course = query_one('SELECT * FROM courses WHERE course_id = %s', (course_id,))
    lecture = query_one(
        'SELECT lid, cid, course_chapter, lec_no, lec_title, lec_summary, lec_url, notes_url FROM lectures WHERE course_chapter = %s AND lec_no = %s',
        (ch, lec_no)
    )

    if request.method == 'POST':
        course_chapter = request.form['course_chapter']
        lec_no = request.form['lec_no']
        title = request.form['lec_title']
        summary = request.form['lec_summary']
        lec_url = request.form['lec_url']
        notes_url = request.form['notes_url']

        query(
            'UPDATE lectures SET course_chapter = %s, lec_no = %s, lec_title = %s, lec_summary = %s, lec_url = %s, notes_url = %s WHERE lid = %s',
            (course_chapter, lec_no, title, summary, lec_url, notes_url, lecture['lid'])
        )
        flash('Lecture updated successfully.')
        return redirect(url_for('admin.manage_lectures', course_id=course_id))
    
    return render_template('admin/lectures/edit_lecture.html', lecture=lecture,course =course, course_id=course_id, params=params)

@bp.route('/<string:course_id>/delete_lecture/<int:lid>')
@admin_required
def delete_lecture(course_id, lid):
    query('DELETE FROM lectures WHERE lid = %s', (lid,))
    flash('Lecture deleted.')
    return redirect(url_for('admin.manage_lectures', course_id=course_id, params=params))