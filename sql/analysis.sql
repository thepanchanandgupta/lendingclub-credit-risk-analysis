SELECT grade,
       COUNT(*) AS total_loans
FROM loans
GROUP BY grade
ORDER BY grade;



SELECT grade,
       AVG(default_flag) AS default_rate
FROM loans
GROUP BY grade
ORDER BY grade;



SELECT purpose,
       COUNT(*) AS total_loans
FROM loans
GROUP BY purpose
ORDER BY total_loans DESC;


SELECT grade,
       AVG(int_rate) AS avg_interest_rate
FROM loans
GROUP BY grade
ORDER BY grade;

SELECT dti_group,
       AVG(default_flag) AS default_rate
FROM loans
GROUP BY dti_group
ORDER BY dti_group;

