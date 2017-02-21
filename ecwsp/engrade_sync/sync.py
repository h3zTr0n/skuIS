from ecwsp.engrade_sync.python_engrade import *
from ecwsp.engrade_sync.models import *

class EngradeSync:
    def __init__(self):
        """ Login and get session from Engrade """
        self.api = PythonEngrade()

    def get_engrade_teacher(self, teacher):
        """ Get an engrade teacher id, create if non existant
        teacher: sis.models.Faculty
        returns teacher's engrade id """
        teacher_sync = TeacherSync.objects.filter(teacher=teacher)
        if not teacher_sync.count():
            pass # Must figure out user creation first
        return teacher_sync.engrade_teacher_id

    def get_engrade_course(self, course, marking_period):
        """ Get an engrade course id, create if non existant. Creates teacher if
        non existant.
        course: schedule.models.Course
        marking_period: unlike SWORD, engrade considers different marking
        periods as different courses
        returns engrade course id"""
        course_sync = CourseSync.objects.filter(course=course, marking_period=marking_period)
        if not course_sync.count():
            name = course.fullname
            syr = course.marking_period.all()[0].school_year.name
            # Figure out gp by determining the order in which the SWORD marking
            # periods occure
            gp = 0
            for mp in course.marking_period.order_by('start_date'):
                gp += 1
                if mp == marking_period:
                    break
            students = ""
            for student in course.get_enrolled_students():
                students += "%s %s %s\n" % (student.fname, student.lname, student.id)
            priteach = self.get_engrade_teacher(course.teacher)
            engrade_id = self.api.schoolclassnew(name, syr, gp, students, priteach)
            course_sync = CourseSync(sword_course=course, engrade_course=engrade_id)
            course_sync.save()
        return course_sync.engrade_teacher_id
