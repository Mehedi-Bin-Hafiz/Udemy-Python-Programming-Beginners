# The contents of a module are made available to the caller using import and from statements.
# when a module is accessed using the import/ from statements, phton performs the following steps:

# 1. search for the module
# 2. Translate the statements in the module into bytecode.
# 3. Create a module object for the module, initially with an empty namespace.
# 4. Execute the bytecode, updating the namespace of the module object.

#syntax
# from module name import class name
# from packagename.module name import class name  # if different package.
# from . import module # if same package


from cals import ad#same package.
c=ad(3, 4)
print(c)
from ModulesAndPackages import Intro # it produce no error
Intro.callme()


######### call module form different package########
##outserder###
from Callable import OuterAdd
print(OuterAdd.outadd(1,2))

from Callable.OuterAdd import outmin ###vvi### class must be after import.
print(outmin.outmin(2,4))

##inner##
from Callable.nested.NestedAdd import inneradd  # here i include NestedAdd module then i can access function directly

print(inneradd(3,9))

from Callable.nested.NestedAdd import mins ### vvi note from packagenam,modulename import classname , mehtod name

print(mins.biyog(3,4))

###syntax##
"""from package_name,module_name import class_name , method_name"""
