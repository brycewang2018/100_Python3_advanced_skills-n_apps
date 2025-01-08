# Student Grade Management Application

<img width="695" alt="image" src="https://github.com/user-attachments/assets/f7920287-9cf5-4c7c-97b3-9bca48a24e1b" />


This is a simple GUI application for managing student grades using Python and `tkinter`. It allows users to input and store grades for four subjects: English, Math, Physics, and Machine Learning. The grades are saved locally in a text file (`students_data.txt`) and can be displayed in a tabular format within the application.

Authoer: Bryce Wang, brycewang2018@gmail.com
## Features

- **Add Student Grades**: Input student name and grades for four subjects.
- **Persistent Storage**: All data is saved in a text file (`students_data.txt`) for later retrieval.
- **Display Data**: View all student records in a dynamically updated table.

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Download the script file (`student_grades.py`).
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script with:

   ```bash
   python student_grades.py
   ```

5. A graphical user interface (GUI) will launch for managing student grades.

## File Structure

- `student_grades.py`: The main application script.
- `students_data.txt`: A file used to store student grade records. This file is automatically created if it doesn't exist.

## Dependencies

This application uses only the built-in Python library `tkinter`, so no additional installations are required.

## Usage

1. Launch the application.
2. Fill in the student's name and grades for each subject.
3. Click the **Add Student** button to save the record.
4. View the added records in the table displayed in the application.

## Future Improvements

- Add functionality to edit or delete student records.
- Provide sorting or filtering options for the table.
- Enhance the UI design for better usability.

## License

This project is open-source and available for use under the MIT License.
