/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <iostream>
#include <vector>
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>
using namespace std;
using namespace boost::python;

class Opqaue {
};

class Item {
  public:
    int x;
    int y;
    Opqaue op;
    Item(const Item& item) {
        cerr << "copy ctor" << endl;
    }
    Item& operator=(const Item& item) {
        cerr << "operator = " << endl;
    }
    Item(int x, int y = 10): x(x), y(y) {}
    void echo(const string& arg = "world") {
        cerr << arg << endl;
    }
    bool operator==(const Item& other) const {
        return other.x == x && other.y == y;
    }
    Opqaue& get_opaque() { return op; }
};
int add(int x, int y) {
    return x + y;
}
using ItemArray = std::vector<Item>;
void handle_item_array(boost::python::list& ss) {
    auto n = boost::python::len(ss);
    for(int i = 0; i < n; i ++) {
        Item& item = boost::python::extract<Item&>(ss[i]);
        cerr << item.x << ", " << item.y << endl;
    }
}

BOOST_PYTHON_MEMBER_FUNCTION_OVERLOADS(Item_overloads, echo, 0, 1);
BOOST_PYTHON_MODULE(test_pye)
{
    class_<Opqaue>("Opqaue");
    class_<Item>("Item",
                 init<int, optional<int>>((args("x"), args("y") = 10)))
            .def_readwrite("x", &Item::x)
            .def_readwrite("y", &Item::y)
            .def("echo", &Item::echo, Item_overloads())
            .def("get_opaque", &Item::get_opaque,
                 return_internal_reference<>())
            ;
    def("add", add);
    def("handle_item_array", &handle_item_array);
    class_<ItemArray>("ItemArray")
            .def(vector_indexing_suite<ItemArray>());
}
