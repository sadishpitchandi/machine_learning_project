'''
to create the own custume classso we want inherit the parent class (excepation) then only we create the own cusme excepation

'''


import os
import sys
                                           #own custume class
class HousingException(Exception):

    def __init__(self,error_meesage:Exception,error_detail:sys):                               #to define some inilizer init fdun 2. error message will the type of exception 3 error details is aviable in sys module we find the line to check the error
        super().__init__(error_meesage)
        self.error_message=HousingException.get_detailed_error_message(error_meesage=error_meesage, error_detail=error_detail)


        ''' 
        if we want to inheriting the  excepatiobn class we need pass some information to parents class=super
         error msg will pass through the excepation class
            2. try to print the error msg
        '''

@staticmethod   # without creating ther object 
def get_detailed_error_message(error_meesage:Exception,error_detail:sys)->str:


    
         """
        error_message: Exception object
        error_detail: object of sys module
        """

    
     _,_ ,exec_tb = error_detail.exc_info()


    ''' 
       most recent excepation   #we need the particulatary tracebrck info 
       (which file is cause the error) so we put first -,-type ,value no need 
    
    '''
    line_number = exec_tb.tb_frame.f_lineno
    file_name=exec_tb.tb_frame.f_code.co_filename
    error_message=f"error occured in scrip: [{file_name}] at line number: [{line_number}] error message: [{error_meesage}]"
    return  error_message


def __str__(self):     #str is try to p[rint the object of any class what informationis displain in print statement defined in str function in dunder method]
    return self.error_message

def __repr__(self) -> str:
    return HousingException.__name__.str()
