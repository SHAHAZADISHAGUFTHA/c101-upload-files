import dropbox
import os

class TransferData:
    def __init__ (self,Access_Token):
        self.Access_Token = Access_Token
        
    def UploadFile (self,file_from,file_to):
        dbx = dropbox.DropBox(self.Access_Token)
        for root, dirs, files in os.walk(file_from):
            relative_path =os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    Access_Token='cl7Y4Cz7LBkAAAAAAAAAAVYEnBJAn2NmIDC_2SxDdPWi79YXg8qh393cw-Oo4vGg'       
    transferData = TransferData(self.Access_Token)

    file_from = input("Enter your file path to upload it on dropbox:    ")
    file_to = input("Enter full path to save it in dropbox:    ")

    transferData.upload_file(file_from, file_to)
main()
    
