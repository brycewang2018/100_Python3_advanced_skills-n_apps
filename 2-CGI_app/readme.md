# Student Grades Management - Python CGI Script

This project is a simple Python CGI script for managing student names and their grades. It demonstrates how to use CGI for form submission and file-based data storage.

=============================================================

<img width="508" alt="image" src="https://github.com/user-attachments/assets/21453b30-8f6e-40d2-b1c1-26d6b3f28453" />
=============================================================

**Author: Bryce Wang, brycewang2018@gmail.com**

## Requirements

1. **Python 3.6 or higher** installed on your system.
2. A basic understanding of terminal commands.
3. An environment to run a simple HTTP server with CGI enabled.


## How to Run

### 1. Set Up the Directory Structure
1. Create a folder for your project.
2. Inside the folder, create a `cgi-bin` directory.
3. Place the `student_grades.py` file inside the `cgi-bin` directory.

### 2. Prepare the `students_data.txt` File
1. In the `cgi-bin` directory, create a blank `students_data.txt` file:
   ```bash
   touch students_data.txt
   chmod 666 students_data.txt
   ```

### 3. Start the HTTP Server
Run the following command in your terminal from the project root directory:
```bash
python3 -m http.server --cgi
```
The server will start on port 8000 by default.

### 4. Access the Script
1. Open your web browser.
2. Go to: `http://localhost:8000/cgi-bin/student_grades.py`

You should see a form to add student names and their grades. Submissions will be saved in the `students_data.txt` file, and a table will display the saved data.

---

## Troubleshooting Common Errors

### Error 1: `403 - CGI script is not executable`
- **Cause**: The script lacks executable permissions.
- **Solution**: Use the command:
  ```bash
  chmod +x cgi-bin/student_grades.py
  ```

### Error 2: `Empty Page`
- **Cause**: Missing or incorrect HTTP response headers in the script.
- **Solution**: Ensure the script begins with:
  ```python
  print("Content-Type: text/html\n")
  ```

### Error 3: `CGI script exit code 127`
- **Cause**: Incorrect shebang (`#!`) in the script.
- **Solution**: Ensure the first line of the script is:
  ```python
  #!/usr/bin/env python3
  ```
  Verify the correct path to Python 3 using:
  ```bash
  which python3
  ```

### Error 4: `Exec format error`
- **Cause**: Incorrect file format (e.g., Windows-style line endings `CRLF`).
- **Solution**: Convert the file to Unix-style `LF` using:
  ```bash
  dos2unix cgi-bin/student_grades.py
  ```

### Error 5: `students_data.txt` Missing or Empty
- **Cause**: The script requires a `students_data.txt` file to store data.
- **Solution**: Create an empty file:
  ```bash
  touch cgi-bin/students_data.txt
  chmod 666 cgi-bin/students_data.txt
  ```

---

## Notes

- Make sure to restart the server after any changes to the script.
- Check terminal logs for detailed error messages if something goes wrong.

---

Feel free to extend or adapt this project to your needs!
