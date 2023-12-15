package com.example;

import com.example.PrintService;

public class MyApplication {
    public static void main(String[] args) {
        new PrintService().print(new MessageModel("Hi!"));
    }
}
