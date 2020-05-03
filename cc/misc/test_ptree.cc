/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <iostream>
#include <fstream>
#include <string>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/ini_parser.hpp>
namespace pt = boost::property_tree;
using namespace std;

void cat(const string &path) {
    ifstream ifs(path.c_str());
    string s;
    while(getline(ifs, s)) {
        cerr << s << endl;
    }
    ifs.close();
}
int main() {
    pt::ptree ptree;
    ptree.put("key1", 10);
    ptree.put("key2", 20.234f);
    ptree.put("key3", "world");
    cerr << ">>>>>write ini<<<<<<" << endl;
    pt::write_ini("/tmp/test_ptree.ini", ptree);
    cat("/tmp/test_ptree.ini");

    pt::ptree ptree2;
    pt::read_ini("/tmp/test_ptree.ini", ptree2);
    assert(ptree2.get<int>("key1") == 10);
    assert(int(ptree2.get<float>("key2")) == 20);
    assert(ptree2.get<string>("key3") == "world");
    return 0;
}
