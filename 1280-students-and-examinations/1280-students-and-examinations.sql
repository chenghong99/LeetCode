# Write your MySQL query statement below

# SELECT s.student_id, s.student_name, sb.subject_name, COUNT(*) AS attended_exams 
# FROM Students s, Subjects sb
# LEFT JOIN Examinations e ON sb.subject_name = e.subject_name AND s.student_id = e.student_id   
# GROUP BY student_id, subject_name

SELECT merge.student_id, merge.student_name, merge.subject_name, COUNT(e.student_id) AS attended_exams
FROM (SELECT *
FROM Students s, Subjects sb) merge 
LEFT JOIN Examinations e ON merge.subject_name = e.subject_name AND merge.student_id = e.student_id   
GROUP BY merge.student_id, merge.subject_name
ORDER BY merge.student_id, merge.subject_name;
