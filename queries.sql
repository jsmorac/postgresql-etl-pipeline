-- 1. Which doctor has the most confirmed appointments?
SELECT doctor_id, COUNT(*) AS confirmed_count
FROM healthtech.appointments
WHERE status = 'confirmed'
GROUP BY doctor_id
ORDER BY confirmed_count DESC
LIMIT 1;

-- 2. How many confirmed appointments does the patient with patient_id '34' have?
SELECT COUNT(*) AS confirmed_count
FROM healthtech.appointments
WHERE patient_id = 34 AND status = 'confirmed';

-- 3. How many cancelled appointments are there between October 21, 2025, and October 24, 2025 (inclusive)?
SELECT COUNT(*) AS cancelled_count
FROM healthtech.appointments
WHERE status = 'cancelled'
  AND booking_date BETWEEN '2025-10-21' AND '2025-10-24';

-- 4. What is the total number of confirmed appointments for each doctor?
SELECT doctor_id, COUNT(*) AS confirmed_count
FROM healthtech.appointments
WHERE status = 'confirmed'
GROUP BY doctor_id
ORDER BY doctor_id;