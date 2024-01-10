#include <Python.h>

/**
 * print_python_bytes - Print information about Python bytes object
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;

    printf("[.] bytes object info\n");
    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; ++i)
        printf("%02x ", (unsigned char)bytes->ob_sval[i]);
    printf("\n");
}

/**
 * print_python_list - Print information about Python list object
 * @p: PyObject pointer to a Python list object
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    PyObject *item;
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; ++i)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyList_Check(item))
            print_python_list(item);
        else if (PyTuple_Check(item))
            printf("tuple\n");
        else if (PyFloat_Check(item))
            printf("float\n");
        else if (PyLong_Check(item))
            printf("int\n");
        else if (PyUnicode_Check(item))
            printf("str\n");
        else
            printf("[ERROR] Unknown Type\n");
    }
}
