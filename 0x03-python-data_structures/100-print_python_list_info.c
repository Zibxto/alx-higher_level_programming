#include <Python.h>

/*
   includes listobject.h
   VIEW HEADER-> https://github.com/python/cpython/blob/master/Include/listobject.h
   VIEW MANUAL-> https://docs.python.org/3.4/c-api/list.html

   includes object.h
   VIEW HEADER-> https://docs.python.org/3.4/c-api/structures.html)
   VIEW MANUAL-> https://github.com/python/cpython/blob/master/Include/object.h
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, index;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (index = 0; index < size; index++)
	{
		printf("Element %ld: %s\n",
				index,
				(PY_TYPE(PyList_GetItem(p, index)))->tp_name);
	}
}
