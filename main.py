import re

def main():
    #テキスト定義
    text = """
Contact list:
John Doe's email is john.doe@example.com.
Jane Smith can be reached at jane.smith@example.org.
For inquiries, please contact info@company.co.uk.
Invalid email: user@.com or @domain.com
"""

    #メアドのパターン定義
    pattern = r"[\w\.-]+@[\w\.-]+"
    emails = re.findall(pattern, text)

    for email in emails:
        print(email)

if __name__ == "__main__":
    main()

