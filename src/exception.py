import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error ocurred in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message
    


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys): #overidden the init method
        super().__init__(error_message) #inheriting from the exception
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self): #print the error message
        return self.error_message
    

    
    