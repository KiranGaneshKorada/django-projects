# importing in-built filters 
from django import template 

register=template.Library() # creating an instance

def myUpper(value):
    result=value[:2].upper()
    return result

# adding custom filter to library
register.filter("myUpper",myUpper)


@register.filter(name="myAppend")
def myAppend(value,arg):
    result=str(arg)+str(value)
    return result


# ANOTHER SYNTAX

"""
from django import template 

register=template.Library()

@register.filter(name="myUpper")
def myUpper(value):
    result=value[:2].upper()
    return result

"""