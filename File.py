# class FILE
class File:
    file_name = '';
    file_location = '';
    
    def __init__(self,in_file_name,in_file_location):
        self.file_name = in_file_name;
        self.file_location = in_file_location;
    
    def get_details(self):
        #print(self.file_name);
        #print(self.file_location);
        print('Full location {}{}'.format(self.file_location,self.file_name));
    
    def open_file(self):
        pass;