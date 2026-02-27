/*
 * File: student_class.cpp
 * Description: Student management system using OOP concepts
 * Author: Atharva
 * Date: 2025-02-15
 */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

// Student class definition
class Student {
private:
    string name;
    int id;
    string department;
    vector<double> grades;
    double gpa;

public:
    // Constructor
    Student(string name = "", int id = 0, string dept = "") 
        : name(name), id(id), department(dept), gpa(0.0) {}

    // Destructor
    ~Student() {
        // Cleanup if needed
    }

    // Setter methods
    void setName(string n) { name = n; }
    void setId(int i) { id = i; }
    void setDepartment(string dept) { department = dept; }
    void addGrade(double grade) {
        grades.push_back(grade);
        calculateGPA();
    }

    // Getter methods
    string getName() const { return name; }
    int getId() const { return id; }
    string getDepartment() const { return department; }
    double getGPA() const { return gpa; }
    vector<double> getGrades() const { return grades; }

    // Calculate GPA
    void calculateGPA() {
        if (grades.empty()) {
            gpa = 0.0;
            return;
        }
        double sum = 0;
        for (double grade : grades) {
            sum += grade;
        }
        gpa = sum / grades.size();
    }

    // Display student information
    void display() const {
        cout << "ID: " << id << endl;
        cout << "Name: " << name << endl;
        cout << "Department: " << department << endl;
        cout << "GPA: " << fixed << setprecision(2) << gpa << endl;
        cout << "Grades: ";
        for (double grade : grades) {
            cout << grade << " ";
        }
        cout << endl;
    }

    // Static method to compare students by GPA
    static bool compareByGPA(const Student& s1, const Student& s2) {
        return s1.gpa > s2.gpa;
    }
};

// Course class
class Course {
private:
    string courseName;
    string courseCode;
    int credits;
    vector<Student> enrolledStudents;

public:
    Course(string name = "", string code = "", int cred = 0)
        : courseName(name), courseCode(code), credits(cred) {}

    void enrollStudent(const Student& student) {
        enrolledStudents.push_back(student);
    }

    void displayStudents() const {
        cout << "\nCourse: " << courseName << " (" << courseCode << ")" << endl;
        cout << "Credits: " << credits << endl;
        cout << "Enrolled Students: " << enrolledStudents.size() << endl;
        
        for (const auto& student : enrolledStudents) {
            cout << "  - " << student.getName() 
                 << " (GPA: " << student.getGPA() << ")" << endl;
        }
    }

    string getCourseName() const { return courseName; }
    vector<Student> getStudents() const { return enrolledStudents; }
};

// Student Management System
class StudentManagementSystem {
private:
    vector<Student> students;
    vector<Course> courses;

public:
    void addStudent(const Student& student) {
        students.push_back(student);
    }

    void removeStudent(int id) {
        auto it = remove_if(students.begin(), students.end(),
            [id](const Student& s) { return s.getId() == id; });
        students.erase(it, students.end());
    }

    Student* findStudent(int id) {
        for (auto& student : students) {
            if (student.getId() == id) {
                return &student;
            }
        }
        return nullptr;
    }

    void displayAllStudents() const {
        cout << "\n===== All Students =====" << endl;
        for (const auto& student : students) {
            student.display();
            cout << "------------------------" << endl;
        }
    }

    void sortStudentsByGPA() {
        sort(students.begin(), students.end(), Student::compareByGPA);
    }

    void displayTopStudents(int n) const {
        cout << "\n===== Top " << n << " Students =====" << endl;
        int count = min(n, (int)students.size());
        for (int i = 0; i < count; i++) {
            cout << i + 1 << ". " << students[i].getName() 
                 << " - GPA: " << students[i].getGPA() << endl;
        }
    }

    int getStudentCount() const { return students.size(); }
};

int main() {
    StudentManagementSystem sms;

    // Create students
    Student s1("John Doe", 1001, "Computer Science");
    s1.addGrade(85.5);
    s1.addGrade(90.0);
    s1.addGrade(88.5);

    Student s2("Jane Smith", 1002, "Mathematics");
    s2.addGrade(92.0);
    s2.addGrade(95.5);
    s2.addGrade(91.0);

    Student s3("Bob Johnson", 1003, "Physics");
    s3.addGrade(78.0);
    s3.addGrade(82.5);
    s3.addGrade(80.0);

    Student s4("Alice Brown", 1004, "Computer Science");
    s4.addGrade(88.0);
    s4.addGrade(91.5);
    s4.addGrade(89.0);

    // Add students to system
    sms.addStudent(s1);
    sms.addStudent(s2);
    sms.addStudent(s3);
    sms.addStudent(s4);

    // Display all students
    sms.displayAllStudents();

    // Find a student
    Student* found = sms.findStudent(1002);
    if (found) {
        cout << "\nFound student:" << endl;
        found->display();
    }

    // Sort and display top students
    sms.sortStudentsByGPA();
    sms.displayTopStudents(3);

    // Remove a student
    sms.removeStudent(1003);
    cout << "\nAfter removing student 1003, total students: " 
         << sms.getStudentCount() << endl;

    return 0;
}

