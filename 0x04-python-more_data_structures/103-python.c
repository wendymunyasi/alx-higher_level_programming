#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	int i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	str = PyBytes_AsString(p);
	printf("  first %d bytes: ", (int)PyBytes_Size(p) + 1);
	for (i = 0; i < PyBytes_Size(p) + 1; i++)
		printf("%02hhx%s", str[i], i + 1 < PyBytes_Size(p) + 1 ? " " : "");
	printf("\n");
}
