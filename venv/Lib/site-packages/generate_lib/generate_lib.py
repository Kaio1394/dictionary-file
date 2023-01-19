from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from enum import Enum
import random
import string

class Color(Enum):
    RED = "\033[31m"
    GREEN = "\033[32m"

class Email_type(Enum):
    hotmail_com_br = "@hotmail.com.br"
    hotmail_com = "@hotmail.com"
    outlook_com_br = "@outlook.com.br"
    outlook_com = "@outlook.com"
    gmail_com_br = "@gmail.com.br"
    gmail_com = "@gmail.com"


def get_type_email(index: int) -> str:
    match index:
        case 1:
            return Email_type.hotmail_com_br.value
        case 2:
            return Email_type.hotmail_com.value
        case 3:
            return Email_type.outlook_com_br.value
        case 4:
            return Email_type.outlook_com.value
        case 5:
            return Email_type.gmail_com_br.value
        case 6:
            return Email_type.gmail_com.value
        case _:
            raise Exception("Option invalid")

@keyword("OUTPUT CONSOLE")
def out_console(text: str, color_green: bool = True):
    """
        OUTPUT CONSOLE      <Message>      <color_green=True>
        Use to generate a color text to console
        Ex: 
            OUTPUT CONSOLE      Navigate to page
            Output:
                STEP - Navigate to page
                This text It'll be green by default.
    """
    color = Color.GREEN.value
    if not color_green: color = Color.RED.value
    BuiltIn().log_to_console(f"{color}"+f"\nSTEP - {text}")


@keyword("INCREMENT VARIABLE")
def increment(variable):
    """
        EX: ${VARIABLE}    GENERATE NUMBER RANDOM      INIT    END
    """
    variable = int(variable)
    return variable + 1


@keyword("GENERATE NUMBER RANDOM")
def random_generate(init=1, end=100) -> int:
    """
        EX: (Int)  GENERATE NUMBER RANDOM       1       10
        EX: (float)  GENERATE NUMBER RANDOM     1.0     10.0
    """
    if type(init) == int and type(end) == int:
        return random.randint(init, end)
    elif type(init) == float and type(end) == float:
        return random.uniform(init, end)
    else:
        raise Exception("Invalid input type.")

@keyword("GENERATE EMAIL RANDOM")
def generate_email_random(type_email: int = 1) -> str:
    """
        GENERATE EMAIL RANDOM       type_email=1
        OUTPUT:
            asdfgcsgscs@hotmail.com.br
    """
    email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "_" + str(random.randint(0, 1000)) + get_type_email(type_email)
    return email

