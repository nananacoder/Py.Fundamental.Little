import os


if __name__ == '__main__':
    f_path = ''
    for file in os.listdir(f_path):
        if file.endswith('.doc'):
            file_path = os.path.join(f_path, file)
            os.system('textutil -convert docx %s' % file_path)