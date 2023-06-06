#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: Pointer to the Python object
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	Py_ssize_t i;
	const char *type;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p)) {
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		type = "compact ascii";
	else
		type = "compact unicode object";

	length = PyUnicode_GET_LENGTH(p);
	printf("  type: %s\n", type);
	printf("  length: %ld\n", length);
	printf("  value: %s\n", PyUnicode_AsUTF8AndSize(p, NULL));
}
