#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <time.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    unsigned char *bytes;
    int limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = (unsigned char *)PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", PyUnicode_AsUTF8AndSize(p, NULL));
    
    limit = size < 10 ? size : 10;
    printf("  first %d bytes: ", limit);
    for (i = 0; i < limit; i++) {
        printf("%02x", bytes[i]);
        if (i != limit - 1)
            printf(" ");
    }
    printf("\n");
}
