#include <Python.h>

/**
 * print_python_list_info - prints information about Python lists
 * @p: pointer to a PyObject (Python object)
 *
 * Description: This function extracts information about a Python list,
 * such as its size, allocated size, and types of elements.
 */

void print_python_list_info(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[*] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *element = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
