import io
from os import write

def write_file(file_name, content):
    '''
    Ghi đè file với 1 dòng nội dung duy nhất
    '''
    f = io.open(file_name, 'w', encoding='utf-8')
    f.write(content)
    f.close()

def write_file_from_list(file_name, list_content):
    '''
    Ghi đè file với nhiều dòng nội dung
    '''
    f = io.open(file_name, 'w', encoding='utf-8')
    f.write('\n'.join(list_content))
    f.close()

def write_file_in_new_line(file_name, content):
    '''
    Ghi vào dòng mới của file với 1 dòng nội dung duy nhất
    '''
    f = io.open(file_name, 'a', encoding='utf-8')
    f.write('\n%s'%content)
    f.close()

if __name__ == '__main__':
    # content = 'Hello world\noke'
    # write_file('abc.txt', content)

    # list_content = ['Dong 1', 'Dong 2', 'Dong 3']
    # write_file_from_list('abc2.txt', list(dict.fromkeys(list_content)))

    content = 'Dong cuoi'
    write_file_in_new_line('abc2.txt', content)