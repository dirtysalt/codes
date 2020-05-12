package com.example.utils;

import org.bson.types.ObjectId;

public final class PeopleModel {
    private ObjectId id;
    private String name;
    private int age;
    public PeopleModel() {
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public ObjectId getId() {
        return id;
    }

    public void setId(ObjectId id) {
        this.id = id;
    }
}
