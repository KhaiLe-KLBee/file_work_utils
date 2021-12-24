import io

def read_content_file(filename):
    '''
    Đọc nội dung file với toàn bộ nội dung được lưu trong 1 biến string
    '''
    f = io.open(filename, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    return content

def read_list_content_file(filename):
    '''
    Đọc nội dung file với toàn bộ nội dung được cắt bởi dấu xuống dòng và được
    lưu vào mảng
    '''
    f = io.open(filename, 'r', encoding='utf-8')
    list_content = f.read()
    f.close()
    return list_content.split('\n')

if __name__ == '__main__':
    # content = read_content_file('abc.txt')
    # print (content)

    list = read_list_content_file('abc2.txt')
    print (list)