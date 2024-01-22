#include <Python.h>

/**
 * print_python_list - Print information about Python lists
 * @p: PyObject pointer representing a Python list
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size, i;
		PyObject *element;

		size = PyList_Size(p);
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; ++i)
		{
			element = PyList_GetItem(p, i);
			printf("Element %ld: ", i);

			if (PyBytes_Check(element))
			{
				printf("bytes\n");
				print_python_bytes(element);
			}
			else if (PyFloat_Check(element))
			{
				printf("float\n");
				print_python_float(element);
			}
			else if (PyTuple_Check(element) || PyList_Check(element))
			{
				printf("tuple\n");
			}
			else
			{
				printf("int\n");
			}
		}
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Print information about Python bytes
 * @p: PyObject pointer representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		Py_ssize_t size, i;
		char *string;

		size = PyBytes_Size(p);
		printf("[.] bytes object info\n");
		printf("  size: %ld\n", size);

		string = PyBytes_AsString(p);
		printf("  trying string: %s\n", string);

		printf("  first 10 bytes: ");
		for (i = 0; i < size && i < 10; ++i)
		{
			printf("%02x ", string[i] & 0xff);
		}
		printf("\n");
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_float - Print information about Python float
 * @p: PyObject pointer representing a Python float object
 */
void print_python_float(PyObject *p)
{
	if (PyFloat_Check(p))
	{
		double value = PyFloat_AsDouble(p);
		printf("[.] float object info\n");
		printf("  value: %f\n", value);
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
	}
}
