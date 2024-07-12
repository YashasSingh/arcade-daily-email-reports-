import os


def read_report_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content
#makes the file open to extract

if __name__ == "__main__":
    # Define the path to the report file
    file_path = 'report.txt'
    
    # Call the function to read the report content
    report_content = read_report_content(file_path)
    
    # Print the content of the report
    print(report_content)
