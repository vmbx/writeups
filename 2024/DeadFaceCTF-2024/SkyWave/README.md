### Skyware 1

- **Description:** In this challenge, the goal was to display tables, describe the **Towers** table, and select the **tower_id** for towers within a specific elevation range.
- **Query:**
  ```sql
  SHOW TABLES;
  DESCRIBE Towers;
  SELECT tower_id FROM Towers WHERE elevation BETWEEN 219.5 AND 220.5;
  ```

![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/SkyWave/SkyWave%201/flag.png)

- **Flag:** `flag{215}`

---

### Skyware 2

- **Description:** The objective was to count the total number of devices that belong to certain device types (smartphone, computer, tablet).
- **Query:**
  ```sql
  SELECT COUNT(*)
  FROM Devices d
  JOIN Device_Types dt ON d.device_type_id = dt.device_type_id
  WHERE dt.device_type_name IN ('smartphone', 'computer', 'tablet');
  ```

![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/SkyWave/SkyWave%202/flag.png)

- **Flag:** `flag{714}`

---

### Skyware 3

- **Description:** The task was to find the most commonly used antenna by **Florian Olyff’s operator**. The result shows the antenna with the highest count.
- **Query:**
  ```sql
  SELECT a.antenna_name, COUNT(*) AS antenna_count
  FROM Towers t
  JOIN Tower_Sectors ts ON t.tower_id = ts.tower_id
  JOIN Antennas a ON ts.antenna_id = a.antenna_id
  WHERE t.operator_id = 4  -- Florian Olyff's operator_id
  GROUP BY a.antenna_name
  ORDER BY antenna_count DESC
  LIMIT 1;
  ```
![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/SkyWave/SkyWave%203/flag.png)

- **Flag:** `flag{Multiple Input Multiple Output (MIMO) 3}`

---

### Skyware 4

- **Description:** The goal was to find the employee number of a technician who worked on Tower 133 on a specific date.
- **Query:**
  ```sql
  SELECT t.employee_number
  FROM Tower_Maintenance tm
  JOIN Technicians t ON tm.technician_id = t.technician_id
  WHERE tm.tower_id = 133
  AND tm.maintenance_date = '2024-08-26';
  ```
![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/SkyWave/SkyWave%204/flag.png)

- **Flag:** `flag{T263739990}`

---

### Skyware 7

- **Description:** This challenge involved retrieving the **IMEI** of a device with a specific device ID.
- **Query:**
  ```sql
  SELECT device_imei
  FROM Devices
  WHERE device_id = 344;
  ```
![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/SkyWave/SkyWave%207/flag.PNG)

- **Flag:** `flag{845303290931675}`

---

### Skyware 9

- **Description:** The objective was to count the number of distinct towers that had a maintenance update.
- **Query:**
  ```sql
  SELECT COUNT(DISTINCT tower_id) 
  FROM Tower_Maintenance 
  WHERE maintenance_type LIKE '%update%';
  ```
![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/SkyWave/SkyWave%209/flag.png)

- **Flag:** `flag{70}`
